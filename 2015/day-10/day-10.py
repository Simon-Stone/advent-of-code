from tqdm import tqdm


def part01(d, n_iter):
    for _ in tqdm(range(n_iter)):
        digits = [c for c in d]
        n_digits = []
        while digits:
            digit = digits.pop(0)
            n_digit = 1
            while digits and digit == digits[0]:
                n_digit += 1
                digits.pop(0)
            n_digits.append((n_digit, digit))
        d = ""
        for n_digit, digit in n_digits:
            d += f"{n_digit}{digit}"
    return d


if __name__ == "__main__":
    test = "1"
    input = "1113222113"

    print(len(part01(input, n_iter=40)))
    print(len(part01(input, n_iter=50)))
