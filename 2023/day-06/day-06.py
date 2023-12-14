import math


def get_distance(button_time, total_time):
    acceleration = 1
    return button_time * acceleration * (total_time - button_time)


def get_num_wins(time, distance):
    delta = math.sqrt((time / 2) ** 2 - distance)
    min_button_time = time / 2 - delta
    max_button_time = time / 2 + delta
    return math.floor(max_button_time) - math.ceil(min_button_time) + 1


def part_01(times, distances):
    num_ways = []
    for time, distance in zip(times, distances):
        num_ways.append(get_num_wins(time, distance + 1))
    return math.prod(num_ways)


def part_02(times, distances):
    time = int("".join(map(str, times)))
    distance = int("".join(map(str, distances)))
    return get_num_wins(time, distance + 1)


if __name__ == "__main__":
    with open("2023/day-06/input.txt") as f:
        times, distances = map(str.strip, f.readlines())
        times = list(map(int, map(str.strip, times.split(":")[1].split())))
        distances = list(map(int, map(str.strip, distances.split(":")[1].split())))

    print(part_01(times, distances))
    print(part_02(times, distances))
