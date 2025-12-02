import math


def factorize(x):
    f = []
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            f.append(i)
            if i * i != x:
                f.append(x / i)
    return f


def calc_n_presents(x):
    factors = factorize(x)
    return sum(factor * 10 for factor in factors)


def part_01(min_presents):
    for x in range(1, 2_000_000):
        n_presents = calc_n_presents(x)
        if n_presents >= min_presents:
            return x


def calc_n_presents_limited(x, exhausted):
    factors = factorize(x)
    return sum(factor * 11 for factor in factors if factor not in exhausted), factors


def part_02(x):
    elves = dict()
    exhausted = set()
    for x in range(1, 2_000_000):
        n_presents, factors = calc_n_presents_limited(x, exhausted=exhausted)
        for factor in factors:
            elves[factor] = elves.get(factor, 0) + 1
            if elves[factor] >= 50:
                exhausted.add(factor)
        if n_presents >= min_presents:
            return x


if __name__ == "__main__":
    min_presents = 34_000_000
    print(part_01(min_presents))
    print(part_02(min_presents))
