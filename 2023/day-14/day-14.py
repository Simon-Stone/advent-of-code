import numpy as np


def part_01(platform):
    platform = tilt_platform(platform)
    return calculate_load(platform)


def part_02(platform):
    n_iter = 1000000000
    history = [platform.copy()]
    for idx in range(1, n_iter + 1):
        platform = spin_cycle(platform)
        if any(np.array_equal(x, platform) for x in history):
            prev_cycle_idx = [
                idx for idx, x in enumerate(history) if np.array_equal(x, platform)
            ][0]
            period_length = idx - prev_cycle_idx
            remainder = (n_iter - prev_cycle_idx) % period_length
            break
        history.append(platform.copy())

    return calculate_load(history[remainder + prev_cycle_idx])


def calculate_load(platform):
    n_rows = platform.shape[0]
    load = 0
    for idx, row in enumerate(platform):
        load += sum(x == "O" for x in row) * (n_rows - idx)
    return load


def parse_input(s):
    return np.array([list(row.strip()) for row in s])


def spin_cycle(platform):
    platform = tilt_platform(platform, direction="N")
    platform = tilt_platform(platform, direction="W")
    platform = tilt_platform(platform, direction="S")
    platform = tilt_platform(platform, direction="E")
    return platform


def tilt_platform(platform, direction="N"):
    if direction == "N":
        return np.array(
            [
                list(
                    "#".join(
                        "".join(sorted(section, reverse=True))
                        for section in "".join(col).split("#")
                    )
                )
                for col in platform.transpose()
            ]
        ).transpose()
    if direction == "W":
        return np.array(
            [
                list(
                    "#".join(
                        "".join(sorted(section, reverse=True))
                        for section in "".join(row).split("#")
                    )
                )
                for row in platform
            ]
        )
    if direction == "S":
        return np.array(
            [
                list(
                    "#".join(
                        "".join(sorted(section)) for section in "".join(col).split("#")
                    )
                )
                for col in platform.transpose()
            ]
        ).transpose()
    if direction == "E":
        return np.array(
            [
                list(
                    "#".join(
                        "".join(sorted(section)) for section in "".join(row).split("#")
                    )
                )
                for row in platform
            ]
        )


if __name__ == "__main__":
    with open("2023/day-14/input.txt") as f:
        platform = parse_input(f.readlines())

    print(part_01(platform))
    print(part_02(platform))
