import re


def part_01(lines):
    return sum(
        [
            int(
                "".join(
                    [
                        re.search(r"\d", line).group(0),
                        re.search(r"\d", line[::-1]).group(0),
                    ]
                )
            )
            for line in lines
        ]
    )


def part_02(lines):
    letters_to_digit = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    digit_words = letters_to_digit.keys()
    reversed_digit_words = [word[::-1] for word in digit_words]
    numbers = []
    for line in lines:
        first = re.search(rf"(?:\d|{'|'.join(digit_words)})", line).group(0)
        if not first.isnumeric():
            first = letters_to_digit[first]

        last = re.search(rf"(?:\d|{'|'.join(reversed_digit_words)})", line[::-1]).group(
            0
        )
        if not last.isnumeric():
            last = letters_to_digit[last[::-1]]
        numbers.append(int("".join([first, last])))
    return sum(numbers)


if __name__ == "__main__":
    with open("./2023/day-01/input.txt") as f:
        lines = f.readlines()
    print(part_01(lines))
    print(part_02(lines))
