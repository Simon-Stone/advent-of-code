from itertools import permutations
from typing_extensions import Self


class Range:

    def __init__(self, s: str):
        self.min, self.max = map(int, s.split("-"))

    def __contains__(self, x):
        return self.min <= x <= self.max

    def __and__(self, other: Self) -> bool:
        return (self.min <= other.min <= self.max) or (
            other.min <= self.max <= other.max
        )

    def __repr__(self) -> str:
        return f"Min: {self.min} Max: {self.max}"

    def __len__(self) -> int:
        return self.max - self.min + 1

    def merge_with(self, other: Self):
        self.min = min(self.min, other.min)
        self.max = max(self.max, other.max)


def is_fresh(ranges: list[Range], ingredient: int) -> bool:
    for range in ranges:
        if ingredient in range:
            return True
    return False


def reduce_ranges(ranges: list[Range]) -> list[Range]:
    fully_reduced = False
    while not fully_reduced:
        for a, b in permutations(ranges, 2):
            if a & b:
                a.merge_with(b)
                ranges.remove(b)
                break
        else:
            fully_reduced = True
    return ranges


if __name__ == "__main__":
    with open("2025/day-05/input.txt") as f:
        ranges_block, ingredients_block = f.read().split("\n\n")
        ranges = [Range(range) for range in ranges_block.splitlines()]
        ingredients = [int(ingredient) for ingredient in ingredients_block.splitlines()]

    print("Part 1:", sum(is_fresh(ranges, ingredient) for ingredient in ingredients))

    print("Part 2:", sum(len(range) for range in reduce_ranges(ranges)))
