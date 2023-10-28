import ctypes


def evaluate(expression, signals):
    if expression.isnumeric():
        return int(expression)

    parts = expression.split()

    if len(parts) == 1:
        return parts[0]

    *operand1, op, operand2 = parts

    if op == "NOT":
        return ctypes.c_uint16(~signals[operand2]).value
    if op == "AND":
        if operand1[0].isnumeric():
            return int(operand1[0]) & signals[operand2]
        return signals[operand1[0]] & signals[operand2]
    if op == "OR":
        return signals[operand1[0]] | signals[operand2]
    if op == "LSHIFT":
        return signals[operand1[0]] << int(operand2)
    if op == "RSHIFT":
        return signals[operand1[0]] >> int(operand2)


def part_01(commands: dict[str, str]):
    signals = {}
    unevaluated = list(commands.items())
    while unevaluated:
        lhs, rhs = unevaluated.pop(0)
        try:
            signals[lhs] = evaluate(rhs, signals)
        except KeyError:
            unevaluated.append((lhs, rhs))

    return signals


if __name__ == "__main__":
    with open("2015/day-07/input.txt") as f:
        input = f.readlines()
    commands = {
        key.strip(): value.strip()
        for value, key in map(lambda x: x.split(" -> "), input)
    }

    print(part_01(commands))
    # print(part_02(input))
