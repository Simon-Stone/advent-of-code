def part01(input):
    n_literals = 0
    n_memory = 0
    for line in input:
        n_literals += len(line)
        n_memory += len(eval(line))
    return n_literals - n_memory


def part02(input):
    n_literals = 0
    n_encode = 0
    for line in input:
        n_literals += len(line)
        n_encode += len(line) + 2 + line.count('"') + line.count("\\")
    print(f"{n_literals=}")
    print(f"{n_encode=}")
    return n_encode - n_literals


if __name__ == "__main__":
    with open("2015/day-08/input.txt") as f:
        input = [line.strip() for line in f.readlines()]
    print(part01(input))
    print(part02(input))
