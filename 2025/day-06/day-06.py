import re


def part_1(rows: list[str]) -> int:
    problems: list[list[str]] = [[] for _ in range(len(rows[1].strip().split()))]
    for row in rows[:-1]:
        for idx, x in enumerate(row.strip().split()):
            problems[idx].append(x)

    total = sum(
        eval(operator.join(problems[idx]))
        for idx, operator in enumerate(rows[-1].strip().split())
    )
    return total


def split_problems(worksheet: list[str]) -> tuple[dict[int, list[str]], dict[int, str]]:
    offset = 0
    operators: dict[int, str] = {}
    problems: dict[int, list[str]] = {}
    for idx, match in enumerate(re.finditer(pattern=r"[*+]\s+", string=worksheet[-1])):
        operator = match.group()
        width = len(operator)
        operators[idx] = operator.strip()
        for row in worksheet[:-1]:
            problems[idx] = problems.get(idx, []) + [row[offset : offset + width]]
        offset += width
    return problems, operators


def rotate_problem(problem: list[str]) -> list[str]:
    rotated_problem = []
    for idx in range(len(problem[0])):
        concatenated_digits = "".join([p[idx] for p in problem[::-1]])
        if concatenated_digits.strip():  # Exclude if string is all whitespace
            rotated_problem.append(concatenated_digits[::-1])
    return rotated_problem


def part_2(rows: list[str]) -> int:
    problems, operators = split_problems(rows)
    rotated_problems = {
        key: rotate_problem(problem) for key, problem in problems.items()
    }
    return sum(
        eval(operators[key].join(problem)) for key, problem in rotated_problems.items()
    )


if __name__ == "__main__":
    with open("2025/day-06/input.txt") as f:
        rows = f.readlines()

    print("Part 1:", part_1(rows))
    print("Part 2:", part_2(rows))
