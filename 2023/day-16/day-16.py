import numpy as np

delta = {
    ">": np.array([0, 1]),
    "v": np.array([1, 0]),
    "<": np.array([0, -1]),
    "^": np.array([-1, 0]),
}


def propagate(beam, layout, beams):
    space = layout[*beam["pos"]]
    if space == ".":
        beam["pos"] += delta[beam["direction"]]
    elif space == "\\":
        if beam["direction"] == ">":
            beam["pos"] += delta["v"]
            beam["direction"] = "v"
        elif beam["direction"] == "<":
            beam["pos"] += delta["^"]
            beam["direction"] = "^"
        elif beam["direction"] == "v":
            beam["pos"] += delta[">"]
            beam["direction"] = ">"
        elif beam["direction"] == "^":
            beam["pos"] += delta["<"]
            beam["direction"] = "<"
    elif space == "/":
        if beam["direction"] == ">":
            beam["pos"] += delta["^"]
            beam["direction"] = "^"
        elif beam["direction"] == "<":
            beam["pos"] += delta["v"]
            beam["direction"] = "v"
        elif beam["direction"] == "v":
            beam["pos"] += delta["<"]
            beam["direction"] = "<"
        elif beam["direction"] == "^":
            beam["pos"] += delta[">"]
            beam["direction"] = ">"
    elif space == "|":
        if beam["direction"] in "<>":
            beams.append({"pos": beam["pos"] + delta["^"], "direction": "^"})
            beam["pos"] += delta["v"]
            beam["direction"] = "v"
        else:
            beam["pos"] += delta[beam["direction"]]
    elif space == "-":
        if beam["direction"] in "^v":
            beams.append({"pos": beam["pos"] + delta["<"], "direction": "<"})
            beam["pos"] += delta[">"]
            beam["direction"] = ">"
        else:
            beam["pos"] += delta[beam["direction"]]
    return beam


def hash_beam(beam):
    return (beam["direction"], tuple(beam["pos"]))


def energize(layout, beams):
    pattern = np.full_like(layout, fill_value=".")
    history = set()
    while beams:
        beam = beams.pop(0)
        if any(beam["pos"] < 0):
            continue
        pattern[*beam["pos"]] = "#"
        try:
            while True:
                beam = propagate(beam, layout, beams)
                if hash_beam(beam) in history or any(beam["pos"] < 0):
                    break
                pattern[*beam["pos"]] = "#"
                history.add(hash_beam(beam))
        except IndexError:
            continue
    return np.unique_counts(pattern).counts[0]


def part_01(layout):
    beams = [{"pos": np.array([0, 0]), "direction": ">"}]
    return energize(layout, beams)


def part_02(layout):
    max_energized = 0
    n_rows = layout.shape[0]
    n_cols = layout.shape[1]
    for x in range(n_rows):
        beams = [{"pos": np.array([x, 0]), "direction": ">"}]
        energized = energize(layout, beams)
        max_energized = max(energized, max_energized)
        beams = [{"pos": np.array([x, n_cols - 1]), "direction": "<"}]
        energized = energize(layout, beams)
        max_energized = max(energized, max_energized)
    for y in range(n_cols):
        beams = [{"pos": np.array([0, y]), "direction": "v"}]
        energized = energize(layout, beams)
        if energized > max_energized:
            max_energized = energized
        beams = [{"pos": np.array([n_rows - 1, y]), "direction": "^"}]
        energized = energize(layout, beams)
        max_energized = max(energized, max_energized)

    return max_energized


if __name__ == "__main__":
    with open("2023/day-16/input.txt") as f:
        layout = np.array(list(map(lambda x: list(x.strip()), f.readlines())))
    print(part_01(layout))
    print(part_02(layout))
