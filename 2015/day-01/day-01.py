from collections import Counter


def part_01(instructions):
    counter = Counter(instructions)
    return counter['('] - counter[')']


def part_02(instructions):
    floor = 0
    up_or_down = {'(': 1, ')': -1}
    for pos, c in enumerate(instructions):
        floor += up_or_down[c]
        if floor == -1:
            return pos+1


if __name__ == '__main__':
    with open('2015/day-01/input.txt') as f:
        instructions = f.readlines()[0]

    print(part_01(instructions))
    print(part_02(instructions))
