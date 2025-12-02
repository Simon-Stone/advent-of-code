from collections import Counter
from dataclasses import dataclass
from itertools import combinations


def part_01(boxes):
    exactly_two = 0
    exactly_three = 0
    for box in boxes:
        counter = Counter(box)
        found_two = found_three = False
        for char, count in counter.items():
            if count == 2 and not found_two:
                exactly_two += 1
                found_two = True
            if count == 3 and not found_three:
                exactly_three += 1
                found_three = True
    return exactly_three * exactly_two


@dataclass
class ID:
    label: str

    def __sub__(self, other):
        diff = 0
        for a, b in zip(self.label, other.label):
            if a != b:
                diff += 1
        return diff

    def __truediv__(self, other):
        common = ""
        for a, b in zip(self.label, other.label):
            if a == b:
                common += a
        return common


def part_02(boxes):
    ids = [ID(box.strip()) for box in boxes]
    for a, b in combinations(ids, 2):
        if (a - b) == 1:
            return a / b


if __name__ == "__main__":
    with open("2018/day-02/input.txt") as f:
        boxes = f.readlines()

    print(part_01(boxes))
    print(part_02(boxes))
