from itertools import cycle


def part_01(ops):
    freq = 0
    for op in ops:
        if op[0] == "+":
            freq += int(op[1:])
        else:
            freq -= int(op[1:])
    return freq


def part_02(ops):
    freq = 0
    prev_freqs = {0}
    for op in cycle(ops):
        if op[0] == "+":
            freq += int(op[1:])
        else:
            freq -= int(op[1:])
        if freq in prev_freqs:
            return freq
        prev_freqs.add(freq)


if __name__ == "__main__":
    with open("2018/day-01/input.txt") as f:
        ops = f.readlines()
    print(part_01(ops))
    print(part_02(ops))
