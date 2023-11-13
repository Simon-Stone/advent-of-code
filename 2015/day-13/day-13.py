import re
import itertools


class Guest:
    def __init__(self, name, left, right, preferences) -> None:
        self.name = name
        self.left = left
        self.right = right
        self.preferences = preferences

    def get_score(self):
        return self.preferences[self.left] + self.preferences[self.right]

    def __repr__(self):
        return f"{self.name=}, {self.left=}, {self.right=}, {self.preferences=}"


def get_guests(x):
    guests = dict()
    for s in x:
        m = re.search(
            r"(.*?) would (.*?) ([0-9]+) happiness units by sitting next to (.*?)\.", s
        )
        name, sign, amount, neighbor = m.groups()
        if sign == "lose":
            amount = -1 * int(amount)
        else:
            amount = int(amount)

        if name not in guests:
            guests[name] = Guest(name, None, None, {neighbor: amount})
        else:
            guests[name].preferences[neighbor] = amount
    return [value for _, value in guests.items()]


def seat_guests(guests):
    # Go through all combinations
    max_total = 0
    for order in itertools.permutations(guests):
        total = 0
        for idx, guest in enumerate(order):
            guest.right = order[(idx + 1) % len(order)].name
            guest.left = order[idx - 1].name
            total += guest.get_score()
        max_total = total if total > max_total else max_total
    return max_total


def part_01(x):
    guests = get_guests(x)
    return seat_guests(guests)


def part_02(x):
    guests = get_guests(x)
    guests.append(Guest("Simon", None, None, dict()))
    for guest in guests[:-1]:
        guest.preferences["Simon"] = 0
        guests[-1].preferences[guest.name] = 0
    return seat_guests(guests)


if __name__ == "__main__":
    with open("./2015/day-13/input.txt") as f:
        s = [line.strip() for line in f.readlines()]
    print(part_01(s))
    print(part_02(s))
