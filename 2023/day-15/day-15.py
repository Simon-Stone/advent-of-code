from collections import OrderedDict


def focusing_power(box_idx, lenses):
    power = 0
    offset = 1 + box_idx
    for idx, (_, lens) in enumerate(lenses.items()):
        power += offset * (idx + 1) * int(lens)
    return power


def hash(s):
    hash_val = 0
    for c in s:
        hash_val += ord(c)
        hash_val *= 17
        hash_val = hash_val % 256
    return hash_val


def part_01(steps):
    return sum(hash(step) for step in steps)


def part_02(steps):
    boxes = {x: OrderedDict() for x in range(256)}
    for step in steps:
        if "=" in step:
            label, lens = step.split("=")
            boxes[hash(label)][label] = lens
        if "-" in step:
            label, _ = step.split("-")
            boxes[hash(label)].pop(label, default=-1)
    return sum(focusing_power(box, lenses) for box, lenses in boxes.items())


if __name__ == "__main__":
    with open("2023/day-15/input.txt") as f:
        s = f.read().split(",")

    print(part_01(s))
    print(part_02(s))
