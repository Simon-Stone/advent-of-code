import re
from collections import Counter
from functools import reduce
from operator import mul

import numpy as np


N_ROWS = 103
N_COLS = 101


def step(robots):
    return [
        (((pos[0] + v[0]) % N_COLS, (pos[1] + v[1]) % N_ROWS), v) for pos, v in robots
    ]


def calc_quadrant(pos):
    if pos[0] == N_COLS // 2 or pos[1] == N_ROWS // 2:
        return None
    if pos[0] < N_COLS // 2 and pos[1] < N_ROWS // 2:
        return 1
    if pos[0] > N_COLS // 2 and pos[1] < N_ROWS // 2:
        return 2
    if pos[0] < N_COLS // 2 and pos[1] > N_ROWS // 2:
        return 3
    return 4


def calc_safety_factor(robots):
    quadrants = [calc_quadrant(robot[0]) for robot in robots]
    count = Counter([quadrant for quadrant in quadrants if quadrant is not None])
    return reduce(mul, count.values())


def part_01(robots):
    for _ in range(100):
        robots = step(robots)
    return calc_safety_factor(robots)


def part_02(robots):
    min_safety_factor = None
    min_step = None
    for n_step in range(1, 10000):
        robots = step(robots)
        safety_factor = calc_safety_factor(robots)
        if min_safety_factor is None or safety_factor < min_safety_factor:
            min_safety_factor = safety_factor
            min_step = n_step
    return min_safety_factor, min_step


if __name__ == "__main__":
    with open("2024/day-14/input.txt") as f:
        robots = []
        for line in f.readlines():
            px, py, vx, vy = re.search(
                r"p=([\d]+),([\d]+) v=([\d-]+),([\d-]+)", line
            ).groups()
            robots.append(((int(px), int(py)), (int(vx), int(vy))))
    print(part_01(robots))
    print(part_02(robots))
