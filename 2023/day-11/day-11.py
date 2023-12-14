import numpy as np

from itertools import combinations


def expand_universe(universe):
    empty_rows = [idx for idx, row in enumerate(universe) if np.all(row == ".")]
    empty_cols = [idx for idx, col in enumerate(universe.T) if np.all(col == ".")]
    rows = sorted([x for x in range(universe.shape[0])] + empty_rows)
    cols = sorted([x for x in range(universe.shape[1])] + empty_cols)
    return universe[rows, :][:, cols]


def get_galaxies(universe):
    return np.argwhere(universe == "#")


def get_distances(galaxies):
    return np.array([np.sum(np.abs(a - b)) for a, b in combinations(galaxies, r=2)])


def part_01(universe):
    universe = expand_universe(universe)
    galaxies = get_galaxies(universe)
    return np.sum(get_distances(galaxies))


def part_02(universe):
    galaxies_before = get_galaxies(universe)
    distances_before = get_distances(galaxies_before)
    galaxies_after = get_galaxies(expand_universe(universe))
    distances_after = get_distances(galaxies_after)
    delta = distances_after - distances_before

    return np.sum(distances_before + 999_999 * delta)


if __name__ == "__main__":
    with open("./2023/day-11/input.txt") as f:
        universe = np.array(list(map(lambda x: [c for c in x.strip()], f.readlines())))
    print(part_01(universe))
    print(part_02(universe))
