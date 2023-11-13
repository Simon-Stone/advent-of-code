import string
from itertools import pairwise


def increment_letter(c, n_steps=1) -> tuple[str, bool]:
    alphabet = string.ascii_lowercase
    idx_c = alphabet.index(c)
    if idx_c + n_steps < len(alphabet):
        return alphabet[idx_c + n_steps], False
    else:
        return alphabet[(idx_c + n_steps) % len(alphabet)], True


def contains_forbidden(pwd):
    return any([x in pwd for x in ["i", "o", "l"]])


def contains_two_pairs(pwd):
    n_pairs = 0
    last_pair = ""
    for x, y in pairwise(pwd):
        if x == y and not x == last_pair:
            n_pairs += 1
            last_pair = x
            continue
        last_pair = ""
    return n_pairs >= 2


def contains_straight(s: str):
    for idx, c in enumerate(s[:-2]):
        c_1, overflow = increment_letter(c)
        if overflow:
            continue
        c_2, overflow = increment_letter(c, 2)
        if overflow:
            continue

        if s[idx + 1] == c_1 and s[idx + 2] == c_2:
            return True
    else:
        return False


def validate_password(pwd: str):
    return (
        len(pwd) == 8
        and pwd.islower()
        and not contains_forbidden(pwd)
        and contains_straight(pwd)
        and contains_two_pairs(pwd)
    )


def increment_password(pwd):
    pwd = [c for c in pwd[::-1]]
    for forbidden_letter in ["i", "o", "l"]:
        if forbidden_letter in pwd:
            forbidden_index = pwd.index(forbidden_letter)
            for idx in range(forbidden_index):
                pwd[idx] = "a"
            pwd[forbidden_index], _ = increment_letter(pwd[forbidden_index])
            return "".join(pwd[::-1])

    for idx in range(len(pwd)):
        pwd[idx], overflow = increment_letter(pwd[idx])
        if not overflow:
            break
    return "".join(pwd[::-1])


def part01(pwd):
    pwd = increment_password(pwd)
    while not validate_password(pwd):
        pwd = increment_password(pwd)
    return pwd


if __name__ == "__main__":
    print(part01("vzbxkghb"))
    print(part01("vzbxxyzz"))
