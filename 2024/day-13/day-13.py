import numpy as np
import re


def part_01(x):
    total_cost = 0
    n_tokens = [3, 1]
    for A, b in machines:
        x = np.linalg.solve(A, b)
        if any(np.abs(x - x.round().astype(int)) > 1e-10):
            continue
        total_cost += sum(x.round() * n_tokens)
    return total_cost


def part_02(x):
    total_cost = 0
    n_tokens = [3, 1]
    for A, b in machines:
        x = np.linalg.solve(A, b + 10000000000000)
        if any(np.abs(x - x.round().astype(int)) > 1e-3):
            continue
        total_cost += sum(x.round() * n_tokens)
    return total_cost


def read_machines(s):
    pattern_button = re.compile(r"\+([0-9]+)")
    pattern_prize = re.compile(r"=([0-9]+)")
    machines = []
    for machine in s.split("\n\n"):
        A = np.array([int(x) for x in re.findall(pattern_button, machine)]).reshape(
            (2, 2), order="F"
        )
        b = np.array([int(x) for x in re.findall(pattern_prize, machine)])
        machines.append((A, b))
    return machines


if __name__ == "__main__":
    with open("2024/day-13/input.txt") as f:
        machines = read_machines(f.read())
    print(part_01(machines))
    print(part_02(machines))
