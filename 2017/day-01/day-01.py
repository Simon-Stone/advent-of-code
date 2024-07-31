from itertools import cycle


def part_01(digits):
    digits = [int(x) for x in digits]
    sum = 0
    for x, y in zip(digits, [*digits[1:], digits[0]]):
        if x == y:
            sum += x
    return sum


def part_02(digits):
    digits = [int(x) for x in digits]
    sum = 0
    steps = len(digits) // 2
    for x, y in zip(digits, [*digits[steps:], *digits[:steps]]):
        if x == y:
            sum += x
    return sum


if __name__ == "__main__":
    with open("2017/day-01/input.txt") as f:
        digits = f.read()

    print(part_01(digits))
    print(part_02(digits))
