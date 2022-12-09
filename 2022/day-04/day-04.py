# Part 1
with open('2022/day-04/input.txt') as f:
    pairs = [pair.strip().split(',') for pair in f.readlines()]


def fully_overlap(a, b):
    a, b = a.split('-'), b.split('-')
    return int(a[0]) <= int(b[0]) and int(a[1]) >= int(b[1])


n_fully_overlapping = 0

for a, b in pairs:
    n_fully_overlapping += fully_overlap(a, b) or fully_overlap(b, a)

print(n_fully_overlapping)


# Part 2
def overlap(a, b):
    a, b = a.split('-'), b.split('-')
    return int(a[0]) <= int(b[0]) and int(a[1]) >= int(b[0])


n_overlapping = 0

for a, b in pairs:
    n_overlapping += overlap(a, b) or overlap(b, a)

print(n_overlapping)