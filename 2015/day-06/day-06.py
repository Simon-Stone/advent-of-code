import re


def part_01(x):
    pass


def part_02(x):
    pass


def parse_input(line):
    print(line)
    match = re.search(r'([a-z\s]*)([0-9]*),([0-9]*) through ([0-9]*),([0-9]*)', line)
    return match.groups()


if __name__ == '__main__':
    with open('2015/day-06/input.txt') as f:
        x = list(map(parse_input, f.readlines()))

    print(x)
    print(part_01(x))
    print(part_02(x))
