def split_directions(directions):
    command, unit = directions.split()
    return (command, int(unit))

with open('Day2-input.txt') as f:
    directions = list(map(split_directions, f.readlines()))
    
depth = 0
horizontal_position = 0
for command, unit in directions:
    if command == 'forward':
        horizontal_position += unit
    elif command == 'down':
        depth += unit
    elif command == 'up':
        depth -= unit

print(f"{horizontal_position * depth}")

depth = 0
horizontal_position = 0
aim = 0
for command, unit in directions:
    if command == 'forward':
        horizontal_position += unit
        depth += aim * unit
    elif command == 'down':
        aim += unit
    elif command == 'up':
        aim -= unit

print(f"{horizontal_position * depth}")