import argparse

def my_sum(numbers: [int]) -> int:
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum

parser = argparse.ArgumentParser(description='Do some stuff main')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=my_sum, default=max,
                        help='sum the integers (default: find the max')

args = parser.parse_args()
print(args.accumulate(args.integers))