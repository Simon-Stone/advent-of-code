def get_max_joltage(bank, n_on):
    start_index = 0
    digits = []
    for i in range(n_on):
        last_index = 1 - (n_on - len(digits))
        if last_index < 0:
            digits.append(max(bank[start_index:last_index]))
        else:
            digits.append(max(bank[start_index:]))
        start_index = start_index + bank[start_index:].index(digits[-1]) + 1
    return int("".join(digits))


if __name__ == "__main__":
    with open("2025/day-03/input.txt") as f:
        banks = [bank.strip() for bank in f.readlines()]

    print("Part 1:", sum(get_max_joltage(bank, n_on=2) for bank in banks))

    print("Part 2:", sum(get_max_joltage(bank, n_on=12) for bank in banks))
