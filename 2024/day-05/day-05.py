from dataclasses import dataclass

    from functools import cmp_to_key, partial


@dataclass
class Page:
    value: int
    rules: dict

    def __lt__(x, y):
        return y.value in rules.get(x.value, [])


def build_rules(rules_string):
    rules = dict()
    for rule in rules_string.split():
        l, r = map(int, rule.split("|"))
        if rules.get(l) is None:
            rules[l] = [r]
        else:
            rules[l].append(r)
    return rules


def compare(a, b, rules):
    if b in rules.get(a, []):
        return -1
    if a in rules.get(b, []):
        return 1
    return 0


def part_01(page_series, rules):
    middle_sum = 0
    for pages in page_series:
        if sorted(pages, key=cmp_to_key(partial(compare, rules=rules))) == pages:
            # middle_sum += pages[len(pages) // 2].value
            middle_sum += pages[len(pages) // 2]
    return middle_sum


def part_02(page_series):
    middle_sum = 0
    for pages in page_series:
        if (sorted_pages := sorted(pages)) != pages:
            middle_sum += sorted_pages[len(sorted_pages) // 2].value
    return middle_sum


if __name__ == "__main__":
    with open("2024/day-04/day-05/input.txt") as f:
        rules, pages = f.read().split("\n\n")
    rules = build_rules(rules)
    # pages = [[Page(int(i), rules) for i in x.split(",")] for x in pages.split()]
    pages = [[int(i) for i in x.split(",")] for x in pages.split()]

    print(part_01(pages, rules))
    # print(part_02(pages))
