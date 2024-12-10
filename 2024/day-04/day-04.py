import numpy as np
import re


def count_xmas(vec):
    s = "".join(vec)
    forward = len(re.findall(r"XMAS", s))
    backward = len(re.findall(r"SAMX", s))
    return forward + backward


def diagonals(grid):
    return [
        np.diagonal(grid, offset) for offset in range(-grid.shape[1] + 1, grid.shape[1])
    ] + [
        np.diagonal(np.fliplr(grid), offset)
        for offset in range(-grid.shape[1] + 1, grid.shape[1])
    ]


def is_x_mas(patch):
    return "".join(patch) in ["MSAMS", "MMASS", "SMASM", "SSAMM"]


def part_01(grid):
    count = 0
    for row in grid:
        count += count_xmas(row)
    for col in grid.T:
        count += count_xmas(col)
    for diag in diagonals(grid):
        count += count_xmas(diag)
    return count


def part_02(grid):
    all_i, all_j = np.where(grid == "A")
    count = 0
    for i, j in zip(all_i, all_j):
        if 0 < i < grid.shape[0] - 1 and 0 < j < grid.shape[0] - 1:
            count += is_x_mas(
                [
                    grid[i - 1, j - 1],
                    grid[i - 1, j + 1],
                    grid[i, j],
                    grid[i + 1, j - 1],
                    grid[i + 1, j + 1],
                ]
            )
    return count


if __name__ == "__main__":
    with open("2024/day-04/input.txt") as f:
        grid = np.array([list(row.strip()) for row in f.readlines()])
    print(part_01(grid))
    print(part_02(grid))
