import re

vowels = 'aeiou'


def part_01(strings):
    nice = 0
    for string in strings:
        if re.search(r'(ab)|(cd)|(pq)|(xy)', string):
            continue
        n_vowels = 0
        for c in string:
            print(c)
            if c in vowels:
                n_vowels += 1
        if n_vowels < 3:
            continue
        if re.search(r'(.)\1', string):
            nice += 1
    return nice


def part_02(strings):
    nice = 0
    for string in strings:
        if re.search(r'([a-z]{2}).*\1', string) and re.search(r'(.)(.){1}\1', string):
            nice += 1
    return nice


if __name__ == '__main__':
    with open("2015/day-05/input.txt") as f:
        strings = f.readlines()

    print(strings)
    print(part_01(strings))
    print(part_02(strings))
