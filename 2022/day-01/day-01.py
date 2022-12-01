""" Find the elfs with the most calories! """
from typing import List

# Unholy (pseudo-)one-liners

# Part 1
with open('2022/day-01/input.txt') as f:
    print(max(map(sum, map(lambda x: map(int, x.split('\n')), f.read().split('\n\n')))))

# Part 2
with open('2022/day-01/input.txt') as f:
    print(sum(sorted(map(sum, map(lambda x: map(int, x.split('\n')), f.read().split('\n\n'))))[-3:]))


def parse_input(input: str) -> List[List[int]]:
    r"""
    Read the puzzle input

    The input is essentially a '\n\n'-separated list of '\n'-separated lists.
    """
    # First split into one '\n'-separated list per elf
    elves = input.split('\n\n')
    # Then split that list
    elves = map(lambda x: x.split('\n'), elves)
    # Return the lists of strings as lists of integers
    return [list(map(int, elf)) for elf in elves]


def sum_calories(elves: List[List[int]]) -> List[int]:
    """ Sums the calories of each elf """
    return list(map(sum, elves))


def part_01(elves: List[List[int]]) -> int:
    """ Finds the largest sum of calories """
    return max(sum_calories(elves))


def part_02(elves: List[List[int]]) -> int:
    """
    Finds the sum of the calories of the three elves
    with the highest calory count.
    """
    top3 = sorted(sum_calories(elves))[-3:]
    return sum(top3)


if __name__ == '__main__':
    with open('2022/day-01/input.txt') as f:
        elves = parse_input(f.read())
    print(part_01(elves))
    print(part_02(elves))
