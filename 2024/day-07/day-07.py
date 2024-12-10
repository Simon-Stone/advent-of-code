from operator import add, mul
from itertools import product


def concat(a, b):
    return int(str(a) + str(b))


def is_solvable(test_value, operands, operators):
    for ops in product(operators, repeat=len(operands) - 1):
        current = operands[0]
        for operand, op in zip(operands[1:], ops):
            current = op(current, operand)
        if current == test_value:
            return True
    return False


def part_01(equations):
    operators = [add, mul]
    return sum(
        [
            test_value
            for test_value, operands in equations
            if is_solvable(test_value, operands, operators)
        ]
    )


def part_02(equations):
    operators = [add, mul, concat]
    return sum(
        [
            test_value
            for test_value, operands in equations
            if is_solvable(test_value, operands, operators)
        ]
    )


if __name__ == "__main__":
    with open("2024/day-07/input.txt") as f:
        equations = []
        for line in f.readlines():
            test_value, operands = line.split(":")
            operands = [int(op) for op in operands.split()]
            test_value = int(test_value)
            equations.append((test_value, operands))

    print(part_01(equations))
    print(part_02(equations))
