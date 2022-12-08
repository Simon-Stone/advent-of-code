import numpy as np

with open('2022/day-08/input.txt') as f:
    grid = np.array([[int(c) for c in line.strip()] for line in f.readlines()])

# Part 1
num_visible = 0
for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        if (grid[:i, j] < grid[i, j]).all() \
            or (grid[i+1:, j] < grid[i, j]).all() \
            or (grid[i, :j] < grid[i, j]).all() \
            or (grid[i, j+1:] < grid[i, j]).all():
            num_visible += 1
print(num_visible)

# Part 2
max_scenic_score = 0
for i in range(1, grid.shape[0]-1):
    for j in range(1, grid.shape[1]-1):
        scenic_score = 1
        for k in range(1, i):
            if grid[i-k, j] >= grid[i, j]:
                scenic_score *= k
                break
        else:
            scenic_score *= i
        for k in range(1, grid.shape[0]-i):
            if grid[i+k, j] >= grid[i, j]:
                scenic_score *= k
                break
        else:
            scenic_score *= grid.shape[0]-i-1
        for k in range(1, j):
            if grid[i, j-k] >= grid[i, j]:
                scenic_score *= k
                break
        else:
            scenic_score *= j
        for k in range(1, grid.shape[1]-j):
            if grid[i, j+k] >= grid[i, j]:
                scenic_score *= k
                break
        else:
            scenic_score *= grid.shape[1]-j-1
        max_scenic_score = scenic_score if scenic_score > max_scenic_score else max_scenic_score
        
print(max_scenic_score)
        
        