def part_01(dimensions):
    area = 0
    for l, w, h in dimensions:
        area += 2*l*w + 2*w*h + 2*h*l
        area += min(l*w, w*h, h*l)
    return area


def part_02(dimensions):
    volume = 0
    perimeter = 0
    for l, w, h in dimensions:
        volume += l*w*h
        perimeter += min(2*l+2*h, 2*l+2*w, 2*h+2*w)
    return volume + perimeter


if __name__ == '__main__':
    with open('2015/day-02/input.txt') as f:
        dimensions = list(map(lambda x: [int(d) for d in x.split('x')], f.readlines()))

    print(part_01(dimensions))
    print(part_02(dimensions))
