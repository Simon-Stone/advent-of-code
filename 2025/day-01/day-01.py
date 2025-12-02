N_NUMBERS = 100
n_zeros = 0
n_zero_crossings = 0


def zero_counting(add):
    def wrapped_add(a, b):
        global n_zeros
        result = add(a, b)
        if result == 0:
            n_zeros += 1
        return result

    return wrapped_add


def zero_crossing_counting(add):
    def wrapped_add(a, b):
        global n_zero_crossings
        result = add(a, b)
        full_rotations = abs((int(a) + int(b)) // N_NUMBERS)
        if (int(a) > 0 and result == 0) or (int(a) < 0 and b == 0):
            full_rotations -= 1
        n_zero_crossings += full_rotations
        return result

    return wrapped_add


class Rotation:
    @staticmethod
    def _parse(s):
        v = int(s[1:])
        if s.startswith("L"):
            v *= -1
        return v

    def __init__(self, s: str):
        self._value = self._parse(s)

    def __int__(self):
        return self._value

    @zero_counting
    @zero_crossing_counting
    def __add__(self, other):
        return (int(self) + int(other)) % N_NUMBERS

    __radd__ = __add__


if __name__ == "__main__":
    with open("2025/day-01/input.txt") as f:
        rotations = [Rotation(s) for s in f.readlines()]

    sum(rotations, 50)
    print(n_zeros)
    print(n_zeros + n_zero_crossings)
