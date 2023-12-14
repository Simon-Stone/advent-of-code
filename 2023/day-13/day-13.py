import numpy as np

from itertools import pairwise


def check_symmetry(matrix, top, bottom):
    while top >= 0 and bottom < matrix.shape[0]:
        if not np.all(matrix[top] == matrix[bottom]):
            return False
        top -= 1
        bottom += 1
    return True


def find_axis(matrix):
    for idx, (a, b) in enumerate(pairwise(matrix)):
        if np.all(a == b):
            if check_symmetry(matrix, idx, idx + 1):
                return idx
    return None


def part_01(patterns):
    left_of_line = 0
    above_line = 0
    for pattern in patterns:
        m = pattern_to_matrix(pattern)
        # Check across rows
        if (row_axis := find_axis(m)) is not None:
            above_line += row_axis + 1
        # Check across columns
        if (col_axis := find_axis(m.T)) is not None:
            left_of_line += col_axis + 1

    return left_of_line + 100 * above_line


def part_02(patterns):
    left_of_line = 0
    above_line = 0
    for pattern in patterns:
        m = pattern_to_matrix(pattern)
        orig_line_row = find_axis(m)
        orig_line_col = find_axis(m.T)
        for idx in np.ndindex(*m.shape):
            m_fixed = m.copy()
            m_fixed[idx] = "#" if m[idx] == "." else "."
            if (fixed_line_row := find_axis(m_fixed)) is not None:
                if orig_line_row != fixed_line_row:
                    above_line += fixed_line_row + 1
                    break
            if (fixed_line_col := find_axis(m_fixed.T)) is not None:
                if orig_line_col != fixed_line_col:
                    left_of_line += fixed_line_col + 1
                    break
    return left_of_line + 100 * above_line


def pattern_to_matrix(pattern):
    rows = pattern.strip().split("\n")
    return np.stack([np.fromiter(row.strip(), dtype=object) for row in rows])


if __name__ == "__main__":
    with open("./2023/day-13/input.txt") as f:
        patterns = f.read().split("\n\n")
    print(part_01(patterns))
    print(part_02(patterns))
