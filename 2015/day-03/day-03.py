def part_01(directions):
    current_house = (0, 0)
    visited = {current_house}
    next_house = {'^': (0, 1), 'v': (0, -1), '>': (1, 0), '<': (-1, 0)}
    for step in directions:
        current_house = (current_house[0] + next_house[step][0], current_house[1] + next_house[step][1])
        visited.add(current_house)
    return len(visited)


def part_02(directions):
    current_house_santa = (0, 0)
    current_house_robo = (0, 0)
    visited = {current_house_santa}
    next_house = {'^': (0, 1), 'v': (0, -1), '>': (1, 0), '<': (-1, 0)}
    for step in directions[::2]:
        current_house_santa = (current_house_santa[0] + next_house[step][0], current_house_santa[1] + next_house[step][1])
        visited.add(current_house_santa)
    for step in directions[1::2]:
        current_house_robo = (current_house_robo[0] + next_house[step][0], current_house_robo[1] + next_house[step][1])
        visited.add(current_house_robo)
    return len(visited)


if __name__ == '__main__':
    with open('2015/day-03/input.txt') as f:
        directions = f.readline()

    print(part_01(directions))
    print(part_02(directions))
