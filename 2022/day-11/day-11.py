import functools
import copy


class Monkey:
    def __init__(self, starting_items, operation, test) -> None:
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.worry_divider = None

    def gets_bored(self):
        if self.worry_divider:
            self.items = [item % self.worry_divider for item in self.items]
        else:
            self.items = [item // 3 for item in self.items]

    def inspect_items(self):
        self.items = [self.operation(item) for item in self.items]
        return len(self.items)

    def throw_items_to(self):
        while self.items:
            yield self.test(self.items[0]), self.items.pop(0)

    def catch(self, item):
        self.items.append(item)


def parse_expression(exp):
    lhs, rhs = exp.split('=')
    match rhs.split():
        case [a, '+', b]:
            if b.isnumeric():
                return lambda x: x + int(b)
            elif a == b:
                return lambda x: x + x
        case [a, '*', b]:
            if b.isnumeric():
                return lambda x: x * int(b)
            elif a == b:
                return lambda x: x * x
    return None


def create_monkey(monkey_string):
    for line in monkey_string.split('\n'):
        l = list(map(str.strip, line.split(':')))
        match l:
            case [_, '']:
                continue
            case ['Starting items', items]:
                items = [int(item) for item in items.split(',')]
            case ['Operation', expression]:
                operation = parse_expression(expression)
            case ['Test', divisible_by]:
                test = divisible_by
            case ['If true', true_action]:
                true_receiver = int(true_action.split('monkey')[-1])
            case ['If false', false_action]:
                false_receiver = int(false_action.split('monkey')[-1])
    divider = int(test.split('by ')[-1])
    test = parse_actions(divider, true_receiver, false_receiver)
    return divider, Monkey(items, operation, test)


def parse_actions(divider, true, false):
    return lambda x: true if x % divider == 0 else false


def monkey_business(monkeys, n_iter):
    n_inspections = [0] * len(monkeys)
    for n in range(n_iter):
        for idx, monkey in enumerate(monkeys):
            n_inspections[idx] += monkey.inspect_items()
            monkey.gets_bored()
            for thrown_to, item in monkey.throw_items_to():
                print(f"Monkey {idx} throws item {item} to monkey {thrown_to}!")
                monkeys[thrown_to].catch(item)
        if (n+1) % 1000 == 0 or (n+1) in [1, 20]:
            print(f"== After round {n+1} ==")
            for idx, monkey in enumerate(monkeys):
                print(f"Monkey {idx} inspected items {n_inspections[idx]} times.")
    return sorted(n_inspections)[-1] * sorted(n_inspections)[-2]


with open('2022/day-11/input.txt') as f:
    monkeys = []
    dividers = []
    for monkey_string in f.read().split('\n\n'):
        divider, monkey = create_monkey(monkey_string)
        dividers.append(divider)
        monkeys.append(monkey)


# Part 1
print(monkey_business(copy.deepcopy(monkeys), 20))


worry_divider = functools.reduce(lambda a, b: a * b, dividers)
# Part 2
for monkey in monkeys:
    monkey.worry_divider = worry_divider
print(monkey_business(monkeys, 10000))
