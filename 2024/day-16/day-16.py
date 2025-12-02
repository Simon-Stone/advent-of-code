import cmath
from collections import deque

DIRECTION = {"N": -1j, "E": 1, "S": 1j, "W": -1}


def part_01(grid, start_pos):
    current_facing = DIRECTION["E"]
    cost_so_far = 0
    unexplored = [
        (start_pos, d, cost_so_far) for d in DIRECTION.values() if d != current_facing
    ]
    unexplored += [(start_pos, current_facing, cost_so_far)]
    unexplored = deque(unexplored)
    while unexplored:
        next_step, current_facing, cost_so_far = unexplored.pop()
        for facing in DIRECTION.values():
            if facing != current_facing:
                cost = (
                    abs(cmath.phase(facing) - cmath.phase(current_facing)) / 90 * 1000
                )
                unexplored.appendleft((next_step, facing, cost_so_far + cost))
            if grid[next_step + facing] == "#":
                return None
            if grid[next_step + facing] == "E":
                return cost_so_far + 1
            if grid[next_step + facing]


def part_02(grid):
    pass


if __name__ == "__main__":
    with open("2024/day-16/test.txt") as f:
        grid = dict()
        for b, line in enumerate(f.readlines()):
            for a, c in enumerate(line.strip()):
                if c == "S":
                    start_pos = a + b * 1j
                    c = "."
                grid[a + b * 1j] = c

    print(part_01(grid, start_pos))
    # print(part_02(grid, start_pos))
