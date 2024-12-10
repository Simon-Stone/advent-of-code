def find_trails(pos, grid):
    to_explore = [pos]
    n_trails = 0
    while to_explore:
        pos = to_explore.pop()
        while grid[pos] != 9:
            to_explore.append(
                [pos + d for d in [-1, 1, 1j, -1j] if grid[pos + d] == grid[pos] + 1]
            )

    return n_trails


def part_01(grid):
    to_explore = [pos for pos, h in grid if h == 0]
    n_trails = 0
    while to_explore:
        n_trails += find_trails(to_explore.pop(), grid)
    return n_trails


def part_02(x):
    pass


if __name__ == "__main__":
    with open("2024/day-10/test.txt") as f:
        grid = dict()
        for im, line in enumerate(f.readlines()):
            for re, c in enumerate(line.strip()):
                grid[re + im * 1j] = int(c)

    print(part_01(grid))
    # print(part_02())
