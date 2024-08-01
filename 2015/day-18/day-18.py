from dataclasses import dataclass
from typing import List
from copy import deepcopy

import numpy as np

TEST_GRID = """.#.#.#
...##.
#....#
..#...
#.#..#
####..
"""


@dataclass
class Light:
    is_on: int = 0

    def __init__(self, is_on):
        self.is_on = is_on

    def switch(self, n_neighbors_on: int):
        if self.is_on and (n_neighbors_on == 2 or n_neighbors_on == 3):
            self.is_on = True
        elif not self.is_on and n_neighbors_on == 3:
            self.is_on = True
        else:
            self.is_on = False

    def __str__(self) -> str:
        return "#" if self.is_on else "."

    @classmethod
    def from_string(cls, s: str):
        return cls(is_on=1 if (s == "#") else 0)


@dataclass
class Grid:
    grid: List[List[Light]] = None

    def __init__(self, grid):
        self.grid = grid
        self.n_x = len(grid[0])
        self.n_y = len(grid)

    def copy(self):
        return Grid(grid=deepcopy(self.grid))

    def n_on(self) -> int:
        n = 0
        for row in self.grid:
            for x in row:
                n += x.is_on
        return n

    @classmethod
    def from_string(cls, s: str):
        grid = []
        for row in s.split("\n"):
            grid.append([Light.from_string(l) for l in row])
        return cls(grid)

    def n_neighbors_on(self, a: int, b: int) -> int:
        n_on = 0
        for x, y in [
            (a - 1, b),
            (a - 1, b - 1),
            (a - 1, b + 1),
            (a, b - 1),
            (a, b + 1),
            (a + 1, b),
            (a + 1, b - 1),
            (a + 1, b + 1),
        ]:
            n_on += self._get_light(x, y)
        return n_on

    def switch(self, sticky_corners=False):
        prev_state = self.copy()
        for x, row in enumerate(self.grid):
            for y, col in enumerate(row):
                if (x, y) in [
                    (0, 0),
                    (0, self.n_y - 1),
                    (self.n_x - 1, 0),
                    (self.n_x - 1, self.n_y - 1),
                ] and sticky_corners:
                    continue
                col.switch(prev_state.n_neighbors_on(x, y))
        return self

    def _get_light(self, x: int, y: int) -> int:
        try:
            if x < 0 or y < 0:
                raise IndexError
            return self.grid[x][y].is_on
        except IndexError:
            return 0

    def __str__(self):
        return "\n".join("".join(map(str, row)) for row in self.grid)


def part_01(x, n_steps):
    g = Grid.from_string(x)
    print(g)
    for _ in range(n_steps):
        g.switch()
        print(g)
    return g.n_on()


def part_02(x, n_steps):
    g = Grid.from_string(x)
    print(g)
    for _ in range(n_steps):
        g.switch(sticky_corners=True)
        print(g)
    return g.n_on()


if __name__ == "__main__":
    with open("2015/day-18/input.txt") as f:
        grid = f.read()
    p1 = part_01(grid, 100)
    p2 = part_02(grid, 100)

    print(p1, p2)
