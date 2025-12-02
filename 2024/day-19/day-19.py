def can_produce(patterns, design):
    if not design:
        return True

    for pattern in patterns:
        if design.startswith(pattern):
            if can_produce(patterns, design[len(pattern) :]):
                return True

    return False


def n_produce(patterns, design):
    if not design:
        return 1

    n_ways = 0
    for pattern in patterns:
        if design.startswith(pattern):
            n_ways += n_produce(patterns, design[len(pattern) :])

    return n_ways


def part_01(patterns, designs)
    return sum(can_produce(patterns, design) for design in designs)


def part_02(patterns, designs):
    return sum(n_produce(patterns, design) for design in designs)


if __name__ == "__main__":

    with open("2024/day-19/input.txt") as f:
        patterns, designs = f.read().split("\n\n")

    patterns = [pattern.strip() for pattern in patterns.split(",")]
    designs = designs.split("\n")

    print(part_01(patterns, designs))
    print(part_02(patterns, designs))
