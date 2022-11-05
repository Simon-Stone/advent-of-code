from itertools import pairwise

with open('Day1-input.txt') as f:
    numbers = list(map(int, f.readlines()))
    
num_increases = sum([y > x for x, y in pairwise(numbers)])
    
print(num_increases)

num_increases = sum([sum(numbers[i:i+3]) < sum(numbers[(i+1):(i+4)]) for i in range(0, len(numbers)-3)])
print(num_increases)
