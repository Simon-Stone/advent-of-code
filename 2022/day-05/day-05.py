import copy
import re

stack_pattern = re.compile(r'\[[A-Z]\]')
command_pattern = re.compile(r'move ([0-9]+) from ([0-9]) to ([0-9])')

crates = list()
commands = list()
with open('2022/day-05/input.txt') as f:
    for line in f.readlines():
        if new_crates := [(match.start() // 4, match.group()) for match in stack_pattern.finditer(line)]:
            crates.append(new_crates)
        
        if match := command_pattern.match(line):
            commands.append([x for x in map(int, match.groups())])

starting_stacks = [list() for _ in range(len(crates[-1]))]
for level in reversed(crates):
    for pos, crate in level:
        starting_stacks[pos].append(crate)

# Part 1
stacks = copy.deepcopy(starting_stacks)
for n, from_, to in commands:
    for _ in range(n):
        stacks[to-1].append(stacks[from_-1].pop())
print(''.join([stack[-1][1] for stack in stacks]))


stacks = copy.deepcopy(starting_stacks)
# Part 2
for n, from_, to in commands:
    stacks[to-1] += stacks[from_-1][-n:]
    del stacks[from_-1][-n:]
print(''.join([stack[-1][1] for stack in stacks]))
