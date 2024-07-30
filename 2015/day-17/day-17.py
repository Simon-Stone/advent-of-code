from itertools import accumulate, combinations


def part_01(sizes):
    egg_nog = 150
    n_combos = 0
    for n_containers in range(len(sizes)):
        for sz in combinations(sizes, r=n_containers):
            if sum(sz) == egg_nog:
                n_combos += 1
    print(n_combos)


def part_02(sizes):
    egg_nog = 150
    n_combos = 0
    for n_containers in range(len(sizes)):
        for sz in combinations(sizes, r=n_containers):
            if sum(sz) == egg_nog:
                n_combos += 1
        if n_combos != 0:
            break
    print(n_combos)


if __name__ == "__main__":
    with open("2015/day-17/input.txt") as f:
        container_sizes = list(map(int, f.readlines()))

    part_01(sorted(container_sizes, reverse=True))
    part_02(sorted(container_sizes, reverse=True))
