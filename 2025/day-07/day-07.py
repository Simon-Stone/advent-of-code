from os import replace


START = 1
BEAM = 1
SPLITTER = "^"
EMPTY = 0

MAPPING = {".": EMPTY, "|": BEAM, "S": START, "^": SPLITTER}


def parse_manifold(manifold_string: list[str]) -> list[list[str | int]]:
    manifold: list[list[str | int]] = []
    for row in manifold_string:
        manifold.append([])
        for c in row.strip():
            manifold[-1].append(MAPPING[c])
    return manifold


def format_manifold(manifold: list[list[str | int]], replace_counts=True) -> str:
    def replace_count(x: int | str) -> str:
        if isinstance(x, str):
            return x
        return "|" if x > 0 else "."

    lines: list[str] = []
    for row in manifold:
        if replace_counts:
            row = [replace_count(c) for c in row]
        lines.append("".join(map(str, row)))
    return "\n".join(lines)


def trace_beam(manifold: list[list[str | int]]) -> list[list[str | int]]:
    for r, row in enumerate(manifold[1:], start=1):
        for c, col in enumerate(row):
            if manifold[r - 1][c] in [EMPTY, SPLITTER]:
                continue
            if col == SPLITTER:
                if not manifold[r][c - 1] == SPLITTER:
                    manifold[r][c - 1] += manifold[r - 1][c]
                if not manifold[r][c + 1] == SPLITTER:
                    manifold[r][c + 1] += manifold[r - 1][c] + manifold[r - 1][c + 1]
            elif col == EMPTY:
                manifold[r][c] += manifold[r - 1][c]
    return manifold


def count_splits(manifold: list[list[str | int]]) -> int:
    n_splits = 0
    for r, row in enumerate(manifold[1:], start=1):
        for c, col in enumerate(row):
            if col == SPLITTER:
                if isinstance(manifold[r - 1][c], int) and manifold[r - 1][c] > 0:
                    n_splits += 1
    return n_splits


def count_timelines(traced_manifold: list[list[str | int]]) -> int:
    return sum(traced_manifold[-1])


if __name__ == "__main__":
    with open("2025/day-07/input.txt") as f:
        manifold = parse_manifold(f.readlines())

    traced_manifold = trace_beam(manifold)
    print("Part 1:", count_splits(traced_manifold))
    print(format_manifold(manifold))
    print("Part 2:", count_timelines(traced_manifold))
    with open("out.txt", "w") as f:
        print(format_manifold(manifold), file=f)
