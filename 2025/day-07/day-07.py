from copy import deepcopy
from dataclasses import dataclass, field


START = "S"
BEAM = "|"
SPLITTER = "^"
EMPTY = "."


def parse_manifold(manifold_string: list[str]) -> list[list[str]]:
    manifold: list[list[str]] = []
    for row in manifold_string:
        manifold.append([])
        for c in row.strip():
            manifold[-1].append(c)
    return manifold


def print_manifold(manifold: list[list[str]]):
    print("-" * len(manifold[0]))
    for row in manifold:
        print("".join(row))
    print("-" * len(manifold[0]))


def trace_beam(manifold: list[list[str]]) -> list[list[str]]:
    for r, row in enumerate(manifold[1:], start=1):
        for c, col in enumerate(row):
            if manifold[r - 1][c] not in [START, BEAM]:
                continue
            if col == SPLITTER:
                if manifold[r][c - 1] == EMPTY:
                    manifold[r][c - 1] = BEAM
                if manifold[r][c + 1] == EMPTY:
                    manifold[r][c + 1] = BEAM
            elif col == EMPTY:
                if manifold[r - 1][c] in [START, BEAM]:
                    manifold[r][c] = BEAM

    return manifold


@dataclass
class State:
    pos: tuple[int, int]
    manifold: list[list[str]]


def count_timelines(manifold: list[list[str]]) -> int:
    starting_point = (1, manifold[0].index(START))
    unexplored: list[State] = [State(pos=starting_point, manifold=deepcopy(manifold))]
    n_timelines = 0
    while unexplored:
        state = unexplored.pop()
        manifold = state.manifold
        starting_row, starting_col = state.pos
        n_timelines += 1
        for r, row in enumerate(manifold[starting_row:], start=starting_row):
            for c, col in enumerate(row):
                if manifold[r - 1][c] not in [START, BEAM]:
                    continue
                if col == SPLITTER:
                    if manifold[r][c + 1] == EMPTY:
                        alternate_manifold = deepcopy(manifold)
                        alternate_manifold[r][c + 1] = BEAM
                        unexplored.append(
                            State(pos=(r + 1, c + 1), manifold=alternate_manifold)
                        )
                    if manifold[r][c - 1] == EMPTY:
                        manifold[r][c - 1] = BEAM

                elif col == EMPTY:
                    manifold[r][c] = BEAM
                    break
        print_manifold(manifold)

    return n_timelines


def count_splits(manifold: list[list[str]]) -> int:
    n_splits = 0
    for r, row in enumerate(manifold[1:], start=1):
        for c, col in enumerate(row):
            if col == SPLITTER:
                if manifold[r - 1][c] == BEAM:
                    n_splits += 1
    return n_splits


if __name__ == "__main__":
    with open("2025/day-07/test.txt") as f:
        manifold = parse_manifold(f.readlines())

    starting_manifold = deepcopy(manifold)
    print("Part 1:", count_splits(trace_beam(manifold)))
    print_manifold(manifold)
    manifold = deepcopy(starting_manifold)
    print("Part 2:", count_timelines(manifold))
