def part_01(grid, pos):
    visited = set()
    direction = 0 - 1j
    while True:
        try:
            if grid[pos + direction] != "#":
                pos += direction
                visited.add(pos)
            else:
                direction *= 1j
        except KeyError:
            break

    return len(visited)


def is_loop(grid, pos):
    visited = set()
    direction = 0 - 1j
    while True:
        try:
            if grid[pos + direction] != "#":
                pos += direction
                if (pos, direction) in visited:
                    return True
                visited.add((pos, direction))
            else:
                direction *= 1j
        except KeyError:
            return False


def part_02(grid, pos):
    n_loops = 0
    for square in grid.keys():
        if grid[square] == "#":
            continue
        grid[square] = "#"
        if is_loop(grid, pos):
            n_loops += 1
        grid[square] = "."
    return n_loops


if __name__ == "__main__":
    grid = dict()
    with open("2024/day-06/input.txt") as f:
        for row, line in enumerate(f.readlines()):
            for col, square in enumerate(line.strip()):
                grid[col + row * 1j] = square
                if square == "^":
                    pos = col + row * 1j

    print(part_01(grid, pos))
    print(part_02(grid, pos))
