import numpy as np
from itertools import permutations


def is_valid_position(pos, grid):
    return 0 <= pos[0] < grid.shape[0] and 0 <= pos[1] < grid.shape[1]


def part_01(grid):
    frequencies = [x for x in np.unique(grid) if x != "."]
    antinode_locations = set()
    for frequency in frequencies:
        for a, b in permutations(zip(*np.where(grid == frequency)), 2):
            a = np.array(a)
            b = np.array(b)
            antinodes = [2 * a - b, 2 * b - a]
            antinode_locations |= set(
                tuple(antinode)
                for antinode in antinodes
                if is_valid_position(antinode, grid)
            )

    return len(antinode_locations)


def part_02(grid):
    frequencies = [x for x in np.unique(grid) if x != "."]
    antinode_locations = set()
    for frequency in frequencies:
        for a, b in permutations(zip(*np.where(grid == frequency)), 2):
            a = np.array(a)
            b = np.array(b)
            inc = 0
            while is_valid_position(antinode := a + inc * (a - b), grid):
                antinode_locations.add(tuple(antinode))
                inc += 1
            while is_valid_position(antinode := b + inc * (b - a), grid):
                antinode_locations.add(tuple(antinode))
                inc += 1

    return len(antinode_locations)


if __name__ == "__main__":
    with open("2024/day-08/input.txt") as f:
        grid = np.array([list(line.strip()) for line in f.readlines()])
    print(part_01(grid))
    print(part_02(grid))
