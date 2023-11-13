import re
import json


def part01(s: str):
    return sum(int(x) for x in re.findall(r"(-*[0-9]+)", s))


def find_value_index(s, value):
    m = re.search(r': "red', s)
    if m:
        return m.start()


def check(j):
    if isinstance(j, int):
        return j
    if isinstance(j, list):
        return sum([check(j) for j in j])
    if not isinstance(j, dict):
        return 0
    if "red" in j.values():
        return 0
    return check(list(j.values()))


def part02(s: str):
    s = json.loads(s)
    return check(s)


if __name__ == "__main__":
    with open("./2015/day-12/input.txt") as f:
        s = f.read()
    print(part01(s))
    print(part02(s))
