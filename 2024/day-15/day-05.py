import numpy as np

DIRECTION = {"^": -1j, ">": 1, "v": 1j, "<": -1}


def make_grid(grid_string):
    grid = dict()
    for b, row in enumerate(grid_string.split("\n")):
        for a, col in enumerate(row):
            if col == "@":
                robot_pos = a + b * 1j
            grid[a + b * 1j] = col
    return grid, robot_pos


def warehouse_string(grid):
    n_rows = int(max(grid.keys(), key=lambda x: x.imag).imag) + 1
    n_cols = int(max(grid.keys(), key=lambda x: x.real).real) + 1
    warehouse = np.empty(shape=(n_rows, n_cols), dtype=str)
    for pos, val in grid.items():
        warehouse[int(pos.imag), int(pos.real)] = val

    warehouse_string = ""
    for row in warehouse:
        warehouse_string += "".join(row)
        warehouse_string += "\n"
    return warehouse_string


def push(grid, pos, direction):
    new_pos = pos + direction
    if grid[new_pos] == ".":
        grid[new_pos] = grid[pos]
        grid[pos] = "."
        return new_pos
    if grid[new_pos] == "#":
        return pos
    if grid[new_pos] == "O":
        new_pos = push(grid, new_pos, direction)
        new_pos -= direction
        if new_pos == pos:
            return pos
        grid[new_pos] = grid[pos]
        grid[pos] = "."
        return new_pos


def gps(grid):
    total = 0
    for pos, val in grid.items():
        if val == "O":
            total += pos.real + 100 * pos.imag
    return total


def resize_grid(grid_string):
    s = (
        grid_string.replace("#", "##")
        .replace("O", "[]")
        .replace(".", "..")
        .replace("@", "@.")
    )
    return make_grid(s)


def part_01(grid, robot_pos, commands):
    for command in commands:
        robot_pos = push(grid, robot_pos, DIRECTION[command])
    return gps(grid)


def part_02(x):
    pass


if __name__ == "__main__":
    with open("2024/day-15/test.txt") as f:
        grid_string, commands = f.read().split("\n\n")
    grid, robot_pos = make_grid(grid_string)
    commands = "".join(commands.split())

    print(part_01(grid, robot_pos, commands))
    grid, robot_pos = resize_grid(grid_string)
    print(warehouse_string(grid))
    # print(part_02())
