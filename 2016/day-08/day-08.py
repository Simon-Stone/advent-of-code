from collections import Counter
from dataclasses import dataclass
import re

import numpy as np
import numpy.typing as npt


@dataclass
class Screen:
    grid: npt.NDArray[np.str_]

    def __init__(self, w: int, h: int):
        self.grid = np.full((h, w), ".")

    def rect(self, w: int, h: int):
        self.grid[:h, :w] = "#"

    def rotate(self, by: int, x: int | None = None, y: int | None = None):
        if x is not None:
            shifted_col = np.roll(self.grid[:, x], shift=by)
            self.grid[:, x] = shifted_col
        if y is not None:
            shifted_row = np.roll(self.grid[y], shift=by)
            self.grid[y] = shifted_row

    def run_instruction(self, instruction: str):
        method, rest = instruction.split(maxsplit=1)
        kwargs: dict[str, int | None] = dict()
        if method == "rect":
            kwargs["w"], kwargs["h"] = map(int, rest.split("x"))
        elif method == "rotate":
            match = re.search(r"([xy])=([0-9]+)", rest)
            if match:
                kwargs[match.group(1)] = int(match.group(2))
            match = re.search(r"by ([0-9]+)", rest)
            if match:
                kwargs["by"] = int(match.group(1))
        getattr(self, method)(**kwargs)

    def __str__(self):
        return "\n".join(["".join(row) for row in self.grid])


def part_01(instructions: list[str]) -> int:
    screen = Screen(w=50, h=6)
    for instruction in instructions:
        screen.run_instruction(instruction)
        print(instruction)
        print(screen)
        print("----" * 5)

    return Counter(screen.grid.flatten())["#"]


def part_02(x):
    pass


if __name__ == "__main__":
    with open("2016/day-08/input.txt") as f:
        instructions = f.read().split("\n")

    print(part_01(instructions))
    # print(part_02())
