# Part 1

with open('2022/day-03/input.txt') as f:
    rucksacks = list(map(str.strip, f.readlines()))
    
exclusives = []
for content in rucksacks:
    comp1, comp2 = content[:len(content)//2], content[len(content)//2:]
    exclusives.append(*set(c for c in comp1 if c in comp2))

total_priority = 0

priority = lambda c: ord(c) - 96 if c.islower() else ord(c) - 38

for c in exclusives:
    total_priority += priority(c)

print(f"Part 1: {total_priority}")

# Part 1 one-liner
from functools import reduce
print(reduce(lambda a, b: sum(map(lambda c: c if isinstance(c, int) else ord(*c) - 96 if str.islower(*c) else ord(*c) - 38, [a, b])), [set(content[:len(content)//2]).intersection(content[len(content)//2:]) for content in rucksacks]))


# Part 2
teams = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]

total_priority = 0
for team in teams:
    total_priority += priority(*set.intersection(*map(set, team)))

print(f"Part 2: {total_priority}")

