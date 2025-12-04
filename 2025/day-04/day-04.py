from typing import Iterator, Self


class Grid:

    def __init__(self, rows: list[str]):
        self._grid = self._parse_grid(rows)

    @staticmethod
    def _parse_grid(rows: list[str]) -> dict[complex, int]:
        grid = dict()
        for im, row in enumerate(rows):
            for re, x in enumerate(row.strip()):
                grid[re + 1j * im] = 0 if x == "." else 1
        return grid

    def get_neighbors(self, center: complex) -> list[int]:
        top = center + (0 - 1j)
        top_left = center + (-1 - 1j)
        left = center + (-1 + 0j)
        bottom_left = center + (-1 + 1j)
        bottom = center + (0 + 1j)
        bottom_right = center + (1 + 1j)
        right = center + (1 + 0j)
        top_right = center + (1 - 1j)
        return [
            self._grid.get(x, 0)
            for x in [
                top,
                top_left,
                left,
                bottom_left,
                bottom,
                bottom_right,
                right,
                top_right,
            ]
        ]

    def is_reachable(self, center: complex) -> bool:
        if self._grid[center] != 1:
            # No roll here
            return False

        n_neighbors = sum(self.get_neighbors(center))
        return n_neighbors < 4

    def get_reachable(self) -> list[complex]:
        return [x for x in self if self.is_reachable(x)]

    def remove_all(self, rolls: list[complex]) -> Self:
        for roll in rolls:
            self._grid[roll] = 0
        return self

    def __iter__(self) -> Iterator[complex]:
        return iter(self._grid.keys())


if __name__ == "__main__":
    with open("2025/day-04/input.txt") as f:
        grid = Grid(f.readlines())

    print("Part 1:", len(grid.get_reachable()))

    reachable_rolls = grid.get_reachable()
    removable_rolls = len(reachable_rolls)
    while len(reachable_rolls) > 0:
        grid.remove_all(reachable_rolls)
        reachable_rolls = grid.get_reachable()
        removable_rolls += len(reachable_rolls)
    print("Part 2:", removable_rolls)
