import numpy as np

with open("2022/day-12/test.txt") as f:
    heightmap = np.array([[c for c in line.strip()] for line in f.readlines()])


to_nums = np.vectorize(lambda x: ord(x))
heightmap = to_nums(heightmap) - 96
heightmap[heightmap == ord('S')-96] = 0
heightmap[heightmap == ord('E')-96] = 27

current_cell = tuple(np.argwhere(heightmap == 0)[0])
print(f"Starting in {current_cell}.")


class Grid:
    def __init__(self, grid) -> None:
        self.options = []    # A list of Tuples[pos, value]
        self.current_path = []
        self.current_cell = (0, 0)
        self.visited = [self.current_cell]
        self.grid = grid

    def clear_options(self):
        self.options.clear()
        return self

    def explore(self):
        row, col = self.current_cell
        if row > 0:
            if abs(self.grid[row-1, col] - self.grid[row, col]) <= 1:
                self.options.append(((row-1, col), self.grid[row-1, col]))
        if row < self.grid.shape[0] - 1:
            if abs(self.grid[row+1, col] - self.grid[row, col]) <= 1:
                self.options.append(((row+1, col), self.grid[row+1, col]))
        if col > 0:
            if abs(self.grid[row, col-1] - self.grid[row, col]) <= 1:
                self.options.append(((row, col-1), self.grid[row, col-1]))
        if col < self.grid.shape[1] - 1:
            if abs(self.grid[row, col+1] - self.grid[row, col]) <= 1:
                self.options.append(((row, col+1), self.grid[row, col+1]))
        return self

    def reset_path(self):
        self.current_path.clear()
        return self

    def sort_options(self):
        self.options = sorted(self.options, key=lambda x: x[1])
        return self

    def move_to(self, cell):
        self.current_cell = cell
        self.visited.append(self.current_cell)
        self.options = [option for option in self.options
                        if option[0] != self.current_cell]


grid = Grid(heightmap)
grid.explore()
print(grid.grid)
print(grid.options)
print(grid.visited)
print('='*5)
grid.move_to(grid.sort_options().options.pop(0)[0])
print(grid.current_cell)
