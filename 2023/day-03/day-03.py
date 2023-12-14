import re


def get_matches(pattern, lines):
    return [list(re.finditer(pattern, line.strip())) for line in lines]


def get_adjacent_squares(matches, offset=0):
    adjacent_squares = set()
    for idx, row in enumerate(matches):
        for match in row:
            if not match:
                continue
            match_pos = match.span()[0]
            for offset_x in [0, -1, 1]:
                for offset_y in [0, -1, 1]:
                    adjacent_squares.add(
                        (idx + offset + offset_x, match_pos + offset_y)
                    )
    return adjacent_squares


def check_number(number, offset, target_squares):
    start, end = number.span()
    for x in range(start, end):
        if (offset, x) in target_squares:
            return True
    return False


def part_01(numbers, symbols):
    adjacent_squares = get_adjacent_squares(symbols)
    sum_adjacents = 0
    for idx, row in enumerate(numbers):
        for number in row:
            if not number:
                continue
            if check_number(number, idx, adjacent_squares):
                sum_adjacents += int(number.group())
    return sum_adjacents


def part_02(numbers, gears):
    gear_ratios = []
    for gear_row_idx, row in enumerate(gears):
        for gear in row:
            adjacent_squares = get_adjacent_squares([[gear]], offset=gear_row_idx)
            adjacent_numbers = []
            for number_row_idx, row in enumerate(numbers):
                if number_row_idx < gear_row_idx - 1:
                    continue
                if number_row_idx > gear_row_idx + 1:
                    break
                for number in row:
                    if not number:
                        continue
                    if check_number(number, number_row_idx, adjacent_squares):
                        adjacent_numbers.append(number)
            if len(adjacent_numbers) == 2:
                gear_ratios.append(
                    int(adjacent_numbers[0].group()) * int(adjacent_numbers[1].group())
                )
    return sum(gear_ratios)


if __name__ == "__main__":
    with open("./2023/day-03/input.txt") as f:
        lines = f.readlines()

    numbers = get_matches(r"[0-9]+", lines)
    symbols = get_matches(r"[^0-9\.]", lines)
    gears = get_matches(r"\*", lines)
    print(part_01(numbers, symbols))
    print(part_02(numbers, gears))
