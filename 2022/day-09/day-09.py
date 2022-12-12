from itertools import pairwise

with open('2022/day-09/input.txt') as f:
    moves = list(map(str.split, f.readlines()))


class Knot:
    def __init__(self, row=0, col=0) -> None:
        self.row = row
        self.col = col

    @property
    def pos(self):
        return (self.row, self.col)

    def is_adjacent(self, other):
        return (abs(self.row - other.row) <= 1) and (abs(self.col - other.col) <= 1)

    def is_up(self, other):
        return self.row > other.row

    def is_down(self, other):
        return self.row < other.row

    def is_right(self, other):
        return self.col > other.col

    def is_left(self, other):
        return self.col < other.col

    def move(self, row_delta, col_delta):
        self.row += row_delta
        self.col += col_delta

    def up(self):
        self.move(1, 0)

    def down(self):
        self.move(-1, 0)

    def right(self):
        self.move(0, 1)

    def left(self):
        self.move(0, -1)


class Rope:
    def __init__(self, n_knots) -> None:
        # The Head is the first element, tail is the last one
        self.knots = [Knot() for _ in range(n_knots)]
        self.visited = set()

    def move(self, direction, distance):
        for _ in range(distance):
            # Move the head
            match direction:
                case 'U':
                    self.knots[0].up()
                case 'D':
                    self.knots[0].down()
                case 'R':
                    self.knots[0].right()
                case 'L':
                    self.knots[0].left()
            # Move the rest
            for a, b in pairwise(self.knots):
                if a.is_adjacent(b):
                    continue
                if a.is_up(b):
                    b.up()
                if a.is_down(b):
                    b.down()
                if a.is_right(b):
                    b.right()
                if a.is_left(b):
                    b.left()
            self.visited.add(self.knots[-1].pos)

    def __str__(self):
        return f"{[knot.pos for knot in self.knots]}"


# Part 1
rope = Rope(2)
print(rope)
for direction, distance in moves:
    rope.move(direction, int(distance))
    print(rope)
print(len(rope.visited))

# Part 2
rope = Rope(10)
for direction, distance in moves:
    rope.move(direction, int(distance))
print(len(rope.visited))
