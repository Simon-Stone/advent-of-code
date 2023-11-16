import copy
import re


class Reindeer:
    def __init__(self, name, speed, fly_period, rest_period) -> None:
        self.name = name
        self.speed = speed
        self.fly_period = fly_period
        self.fly_time = 0
        self.distance_traveled = 0
        self.rest_period = rest_period
        self.rest_time = 0
        self.is_resting = False
        self.points = 0

    def __repr__(self):
        return f"{self.name=}, {self.distance_traveled=}, {self.points=}"

    def __eq__(self, other):
        return self.distance_traveled == other.distance_traveled

    def __ne__(self, other) -> bool:
        return not self == other

    def __gt__(self, other):
        return self.distance_traveled > other.distance_traveled

    def __lt__(self, other):
        return self.distance_traveled < other.distance_traveled


def parse_reindeer(s):
    m = re.match(
        r"([A-Za-z]*) can fly ([0-9]+) km/s for ([0-9]+) seconds, but then must rest for ([0-9]+) seconds.",
        s,
    )
    return Reindeer(
        name=m.group(1),
        speed=int(m.group(2)),
        fly_period=int(m.group(3)),
        rest_period=int(m.group(4)),
    )


def part_01(x: list[Reindeer]):
    for tic in range(1, 2504):
        for reindeer in x:
            if reindeer.rest_period == reindeer.rest_time:
                reindeer.rest_time = 0
                reindeer.fly_time = 0
                reindeer.is_resting = False
            if reindeer.is_resting:
                reindeer.rest_time += 1
                continue
            reindeer.fly_time += 1
            reindeer.distance_traveled += reindeer.speed
            if reindeer.fly_period == reindeer.fly_time:
                reindeer.is_resting = True
            print(
                f"{reindeer.name}: {reindeer.distance_traveled}, {reindeer.is_resting}"
            )
    return max(x)


def max_points(reindeer: list[Reindeer]):
    max_p = 0
    for r in reindeer:
        if r.points > max_p:
            max_p = r.points
    return max_p


def part_02(x: list[Reindeer]):
    for tic in range(1, 2504):
        for reindeer in x:
            if reindeer.rest_period == reindeer.rest_time:
                reindeer.rest_time = 0
                reindeer.fly_time = 0
                reindeer.is_resting = False
            if reindeer.is_resting:
                reindeer.rest_time += 1
                continue
            reindeer.fly_time += 1
            reindeer.distance_traveled += reindeer.speed
            if reindeer.fly_period == reindeer.fly_time:
                reindeer.is_resting = True
        lead = max(x)
        for reindeer in x:
            if reindeer.distance_traveled == lead.distance_traveled:
                reindeer.points += 1
    return max_points(x)


if __name__ == "__main__":
    with open("2015/day-14/input.txt") as f:
        reindeer = [parse_reindeer(line) for line in f.readlines()]
    print(part_01(copy.deepcopy(reindeer)))
    print(part_02(copy.deepcopy(reindeer)))
