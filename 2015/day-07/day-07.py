def AND(op1, op2):
    return get_value(op1) & get_value(op2)


def OR(op1, op2):
    return get_value(op1) | get_value(op2)


def LSHIFT(op1, op2):
    return get_value(op1) << op2


def RSHIFT(op1, op2):
    return get_value(op1) >> op2


def NOT(op):
    return ~get_value(op)


def get_value(expression):
    if expression.isnumeric():
        return int(expression)

    parts = expression.split()
    if len(parts) == 1:
        return get_value(commands[parts[0]])

    *operand1, op, operand2 = parts

    if op == 'NOT':
        return NOT(operand2)
    if op == 'AND':
        return AND(*operand1, operand2)
    if op == 'OR':
        return OR(*operand1, operand2)
    if op == 'LSHIFT':
        return LSHIFT(*operand1, int(operand2))
    if op == 'RSHIFT':
        return RSHIFT(*operand1, int(operand2))


def part_01(commands):
    new_level = False
    while new_level:
        new_level = False
        for signal, level in commands.items():
            if isinstance(level, int):
                continue
            if level.isnumeric():
                commands[signal] = int(level)
                new_level = True
                continue
            parts = level.split()
            if len(parts) == 1:
                commands[signal] = commands[parts[0]]
            if len(parts) == 2:
                if isinstance(commands[parts[1]], int):
                    commands[signal] = ~commands[parts[1]]
            if 
    
    return commands['a']


def part_02(x):
    pass


if __name__ == '__main__':
    with open('2015/day-07/input.txt') as f:
        input = f.readlines()
    commands = {key.strip(): value.strip() for value, key in map(lambda x: x.split(' -> '), input)}
    
    print(part_01(commands))
    print(part_02(input))
