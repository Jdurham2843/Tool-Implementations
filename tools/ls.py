# ls man page - http://linuxcommand.org/lc3_man_pages/ls1.html
import sys
import argparse

from pathlib import Path

# LS success/error return codes
SUCCESSFUL = 0
MINOR_ERROR = 1
MAJOR_ERROR = 2

ARGS = None
def parse_arguments():
    parser = argparse.ArgumentParser(description='ls help')
    parser.add_argument('directory', metavar='D', type=str, nargs='?', default='.')
    parser.add_argument('-a', '--all', dest='get_viewable_files', action='store_const',
                               const=show_all, default=filter_files, 
                               help='do not ignore entries starting with .')
    global ARGS 
    ARGS = parser.parse_args()

def show_all(initial_directory: Path) -> [Path]:
    return [file for file in initial_directory.iterdir()]

def filter_files(initial_directory: Path) -> [Path]:
    return [file for file in initial_directory.iterdir() if '.' not in file.stem]

class DirectoryContext:
    def __init__(self, directory_path, arguments):
        self.directory_path = directory_path
        self.arguments = arguments

def construct_directory_context() -> DirectoryContext:
    path_argument = ARGS.directory
    return DirectoryContext(Path(path_argument), list())

def show_directory(directory_context: DirectoryContext) -> int:
    path = directory_context.directory_path
    if (not path.is_dir()):
        return MAJOR_ERROR

    files_to_show = ARGS.get_viewable_files(path)
    [print(file.name) for file in files_to_show]

    return SUCCESSFUL

def do_work() -> int:
    directory_context = construct_directory_context()
    code = show_directory(directory_context)

    if (code != SUCCESSFUL):
        print('There was a problem')
    
    return code
    
if __name__ == '__main__':
    parse_arguments()
    code = do_work()
    exit(code)