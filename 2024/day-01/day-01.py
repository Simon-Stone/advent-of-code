import numpy as np
from collections import Counter


def part_01(lists: np.array) -> int:
    lists.sort(axis=0)
    return sum(np.abs(lists[:, 0] - lists[:, 1]))


def part_02(lists):
    left = lists[:, 0]
    freq = Counter(lists[:, 1])
    total = 0
    for x in left:
        total += freq[x] * x
    return total


if __name__ == "__main__":

    with open("2024/day-01/test.txt") as f:
        lists = np.array(list(map(str.split, f.readlines()))).astype("int")

    print(part_01(lists))
    print(part_02(lists))
