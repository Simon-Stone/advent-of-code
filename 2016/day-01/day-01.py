def part_01(x):
    headings = ["N", "E", "S", "W"]
    current_heading_idx = 0
    pos = [0, 0]
    for instruction in x:
        direction, n = instruction.strip()[0], int(instruction.strip()[1:])
        if direction == "R":
            current_heading_idx = (current_heading_idx + 1) % len(headings)
        if direction == "L":
            current_heading_idx = current_heading_idx - 1
            if current_heading_idx < 0:
                current_heading_idx = len(headings) + current_heading_idx

        if headings[current_heading_idx] == "N":
            pos[0] += n
        elif headings[current_heading_idx] == "S":
            pos[0] -= n
        elif headings[current_heading_idx] == "E":
            pos[1] += n
        elif headings[current_heading_idx] == "W":
            pos[1] -= n
    return sum(pos)


def part_02(x):
    headings = ["N", "E", "S", "W"]
    current_heading_idx = 0
    history = set()
    pos = [0, 0]
    history.add(tuple(pos))
    for instruction in x:
        direction, n = instruction.strip()[0], int(instruction.strip()[1:])
        if direction == "R":
            current_heading_idx = (current_heading_idx + 1) % len(headings)
        if direction == "L":
            current_heading_idx = current_heading_idx - 1
            if current_heading_idx < 0:
                current_heading_idx = len(headings) + current_heading_idx

        if headings[current_heading_idx] == "N":
            pos[0] += n
        elif headings[current_heading_idx] == "S":
            pos[0] -= n
        elif headings[current_heading_idx] == "E":
            pos[1] += n
        elif headings[current_heading_idx] == "W":
            pos[1] -= n
        if tuple(pos) in history:
            return sum(pos)
        history.add(tuple(pos))
    return None


if __name__ == "__main__":
    with open("./2016/day-01/input.txt") as f:
        instructions = f.read().strip().split(",")

    print(part_01(instructions))
    print(part_02(["R8", "R4", "R4", "R8"]))
