import copy


def get_sum_next(histories, reverse=False):
    sum_next = 0
    for history in histories:
        diff_sequences = [history]
        diff_sequence = [history[i + 1] - history[i] for i in range(len(history) - 1)]
        diff_sequences.append(diff_sequence)
        while any(diff_sequence):
            diff_sequence = [
                diff_sequence[i + 1] - diff_sequence[i]
                for i in range(len(diff_sequence) - 1)
            ]
            diff_sequences.append(diff_sequence)
        diff_sequences = diff_sequences[::-1]
        if reverse:
            diff_sequences = [s[::-1] for s in diff_sequences]
        for i in range(len(diff_sequences) - 1):
            if reverse:
                new_value = diff_sequences[i + 1][-1] - diff_sequences[i][-1]
            else:
                new_value = diff_sequences[i + 1][-1] + diff_sequences[i][-1]
            diff_sequences[i + 1].append(new_value)
        sum_next += diff_sequences[-1][-1]
    return sum_next


def part_01(histories):
    return get_sum_next(histories)


def part_02(x):
    return get_sum_next(histories, reverse=True)


if __name__ == "__main__":
    with open("2023/day-09/input.txt") as f:
        histories = list(
            map(list, map(lambda x: map(int, x), map(str.split, f.readlines())))
        )
    print(part_01(copy.deepcopy(histories)))
    print(part_02(copy.deepcopy(histories)))
