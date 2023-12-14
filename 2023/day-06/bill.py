#!/usr/bin/python3

# This is a set of two equations in two variables which we can solve
# for the end points of the winning range.
#
# T = total time (given time)
# D = winning distance (i.e. given distance + 1).
# b = button press time (which is also speed)
# r = run time
#
# T = b + r
# D = b * r
#
# Rearranging
# b^2 -Tb + D = 0
#
# Quadratic formula
# b = (T +/- sqrt(T^2 - 4D) / 2

from math import sqrt, floor, ceil


def waystowin(T, D):
    x = sqrt(T**2 - 4 * D)
    r1 = (T - x) / 2
    r2 = (T + x) / 2
    return len(range(floor(r2) - ceil(r1))) + 1


# List of sublists
races = []
with open("2023/day-06/test.txt", "r") as inputfile:
    times = [int(t) for t in inputfile.readline().split()[1:]]
    distances = [int(d) for d in inputfile.readline().split()[1:]]
    for race in range(len(times)):
        races.append([times[race], distances[race]])

part1 = 1
for r in races:
    part1 *= waystowin(r[0], r[1] + 1)
print("Part 1 ways to win:", part1)

# Convert input for part 2
race2 = [
    int("".join([str(t[0]) for t in races])),
    int("".join([str(t[1]) for t in races])),
]
print("Part 2 ways to win:", waystowin(race2[0], race2[1] + 1))
