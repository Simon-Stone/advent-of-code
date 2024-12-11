from collections import deque


def rule_one(stone):
    if stone == 0:
        return (1,)
    return (None,)


def rule_two(stone):
    stone = str(stone)
    if len(stone) % 2 == 0:
        return int(stone[: len(stone) // 2]), int(stone[len(stone) // 2 :])
    return (None,)


def rule_three(stone):
    return (stone * 2024,)


def blink(stones):
    after_blink = deque()
    for stone in stones:
        for rule in [rule_one, rule_two, rule_three]:
            a, *b = rule(stone)
            if a is not None:
                after_blink.append(a)
                after_blink.extend(b)
                break
    return after_blink


def part_01(stones):
    n_blinks = 25
    for _ in range(n_blinks):
        stones = blink(stones)
    return len(stones)


def part_02(stones):
    n_blinks = 75
    for _ in range(n_blinks):
        stones = blink(stones)
    return len(stones)


if __name__ == "__main__":
    with open("2024/day-11/input.txt") as f:
        stones = [int(c) for c in f.read().split()]
    print(part_01(stones))
    print(part_02(stones))
