def part_01(lines):
    keypad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    pos = [1, 1]
    code = []
    for line in lines:
        for step in line:
            if step == "U":
                pos[0] = max(0, pos[0] - 1)
            elif step == "D":
                pos[0] = min(2, pos[0] + 1)
            elif step == "L":
                pos[1] = max(0, pos[1] - 1)
            elif step == "R":
                pos[1] = min(2, pos[1] + 1)
        code.append(keypad[pos[0]][pos[1]])
    return code


def part_02(x):
    keypad = [
        [-1, -1, 1, -1, -1],
        [-1, 2, 3, 4, -1],
        [5, 6, 7, 8, 9],
        [-1, "A", "B", "C", -1],
        [-1, -1, "D", -1, -1],
    ]
    pos = [2, 0]
    code = []
    for line in lines:
        for step in line:
            if step == "U":
                new_pos = max(0, pos[0] - 1)
                if keypad[new_pos][pos[1]] != -1:
                    pos[0] = new_pos
            elif step == "D":
                new_pos = min(4, pos[0] + 1)
                if keypad[new_pos][pos[1]] != -1:
                    pos[0] = new_pos
            elif step == "L":
                new_pos = max(0, pos[1] - 1)
                if keypad[pos[0]][new_pos] != -1:
                    pos[1] = new_pos
            elif step == "R":
                new_pos = min(4, pos[1] + 1)
                if keypad[pos[0]][new_pos] != -1:
                    pos[1] = new_pos
        code.append(keypad[pos[0]][pos[1]])
    return code


if __name__ == "__main__":
    with open("2016/day-02/input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(part_01(lines))
    print(part_02(lines))
