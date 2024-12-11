import numpy as np


def part_01(reports):
    n_safe = 0
    for report in reports:
        diff = np.abs(np.diff(report))
        if (
            (
                np.all(np.sort(report) == report)
                or np.all(np.sort(report)[::-1] == report)
            )
            and np.all(0 < diff)
            and np.all(diff < 4)
        ):
            n_safe += 1
    return n_safe


def part_02(x):
    n_safe = 0
    for report in reports:
        diff = np.abs(np.diff(report))
        if (
            (
                np.all(np.sort(report) == report)
                or np.all(np.sort(report)[::-1] == report)
            )
            and np.all(0 < diff)
            and np.all(diff < 4)
        ):
            n_safe += 1
        else:
            for i in range(report.shape[0]):
                dampened_report = np.delete(report, i)
                diff = np.abs(np.diff(dampened_report))
                if (
                    (
                        np.all(np.sort(dampened_report) == dampened_report)
                        or np.all(np.sort(dampened_report)[::-1] == dampened_report)
                    )
                    and np.all(0 < diff)
                    and np.all(diff < 4)
                ):
                    n_safe += 1
                    break

    return n_safe


if __name__ == "__main__":

    with open("2024/day-02/input.txt") as f:
        reports = [np.array(line.split()).astype("int") for line in f.readlines()]

    print(part_01(reports))
    print(part_02(reports))
