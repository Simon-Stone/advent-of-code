def get_start(diagram):
    for i, row in enumerate(diagram):
        for j, col in enumerate(row):
            if col == "S":
                return i, j
    return None, None


def can_east(diagram, x, y):
    return diagram[x][y] in "S-LF" and diagram[x][y + 1] in "S-J7"


def can_west(diagram, x, y):
    return diagram[x][y] in "S-J7" and diagram[x][y - 1] in "S-LF"


def can_north(diagram, x, y):
    return diagram[x][y] in "S|LJ" and diagram[x - 1][y] in "S|F7"


def can_south(diagram, x, y):
    return diagram[x][y] in "S|F7" and diagram[x + 1][y] in "S|LJ"


def find_next(diagram, x, y, visited):
    if can_east(diagram, x, y) and (x, y + 1) not in visited:
        return x, y + 1
    if can_south(diagram, x, y) and (x + 1, y) not in visited:
        return x + 1, y
    if can_west(diagram, x, y) and (x, y - 1) not in visited:
        return x, y - 1
    if can_north(diagram, x, y) and (x - 1, y) not in visited:
        return x - 1, y


def part_01(diagram):
    current_row, current_col = get_start(diagram)
    visited = set()
    count = 0
    next_row, next_col = find_next(diagram, current_row, current_col, visited)
    while diagram[next_row][next_col] != "S":
        count += 1
        visited.add((next_row, next_col))
        next_row, next_col = find_next(diagram, next_row, next_col, visited)
    return round(len(visited) / 2)


def part_02(x):
    pass


if __name__ == "__main__":
    with open("./2023/day-10/input.txt") as f:
        diagram = list(map(lambda x: [c for c in x.strip()], f.readlines()))

    print(part_01(diagram))
    print(part_02())
