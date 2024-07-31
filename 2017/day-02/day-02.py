from itertools import permutations


def parse_input(x):
    rows = [list(map(int, row.split())) for row in x.strip().split("\n")]
    return rows


def find_evens(numbers):
    for x, y in permutations(numbers, r=2):
        if x % y == 0:
            return x / y
        if y % x == 0:
            return y / x


def part_01(x):
    spreadsheet = parse_input(x)
    diff = 0
    for row in spreadsheet:
        diff += max(row) - min(row)
    return diff


def part_02(x):
    spreadsheet = parse_input(x)
    sum = 0
    for row in spreadsheet:
        sum += find_evens(row)
    return sum


if __name__ == "__main__":
    with open("2017/day-02/input.txt") as f:
        spreadsheet = f.read()

    print(part_01(spreadsheet))
    print(part_02(spreadsheet))
