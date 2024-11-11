from itertools import permutations
import numpy as np


def validate_triangle(a, b, c):
    return all(x + y > z for x, y, z in permutations((a, b, c)))


def part_01(triangles):
    return sum(validate_triangle(*triangle) for triangle in triangles)


def part_02(triangles):
    triangles = np.array(list(triangles)).reshape((3, -1), order="F").transpose()
    return sum(validate_triangle(*triangle) for triangle in triangles)


if __name__ == "__main__":
    with open("2016/day-03/input.txt") as f:
        triangles = list(list(map(int, x)) for x in map(str.split, f.readlines()))
    print(part_01(triangles))
    print(part_02(triangles))
