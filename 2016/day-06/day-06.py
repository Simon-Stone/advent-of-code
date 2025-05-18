from collections import Counter

import numpy as np
import numpy.typing as npt


def part_01(messages: npt.ArrayLike) -> str:
    corrected_message: list[str] = []
    for col in messages.T:
        c, _ = Counter(col).most_common(n=1)[0]
        corrected_message.append(c)
    return "".join(corrected_message)


def part_02(messages: npt.ArrayLike) -> str:
    corrected_message: list[str] = []
    for col in messages.T:
        c, _ = Counter(col).most_common()[-1]
        corrected_message.append(c)
    return "".join(corrected_message)


if __name__ == "__main__":
    with open("2016/day-06/input.txt") as f:
        messages = np.array([[c for c in line.strip()] for line in f.readlines()])

    print(part_01(messages))
    print(part_02(messages))
