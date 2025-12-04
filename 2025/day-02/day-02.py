from itertools import batched


class ID:
    def __init__(self, id: int):
        self._value = str(id)

    def is_invalid(self):

        if (n_id := len(self._value)) % 2 == 0:
            return self._value[: n_id // 2] == self._value[n_id // 2 :]
        return False

    def is_really_invalid(self):
        n_id = len(self._value)
        for idx in range(1, n_id // 2 + 1):
            chunks = [*batched(self._value, idx)]
            if len(set(chunks)) == 1:
                return True
        return False


if __name__ == "__main__":

    with open("2025/day-02/input.txt") as f:
        ranges = f.read().split(",")

    invalid_ids = []
    really_invalid_ids = []
    for id_range in ranges:
        min, max = id_range.split("-")
        invalid_ids.extend(
            [x for x in range(int(min), int(max) + 1) if ID(x).is_invalid()]
        )
        really_invalid_ids.extend(
            [x for x in range(int(min), int(max) + 1) if ID(x).is_really_invalid()]
        )

    print("Part 1:", sum(invalid_ids))
    print("Part 2:", sum(really_invalid_ids))
