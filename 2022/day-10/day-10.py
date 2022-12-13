with open('2022/day-10/input.txt') as f:
    program = [line.strip().split() for line in f.readlines()]


def calc_signal_strength(cycle, X, signal_strength):
    if (cycle - 20) % 40 == 0:
        signal_strength += cycle * X
    return signal_strength


X = 1
cycle = 0
signal_strength = 0

for line in program:
    cycle += 1
    signal_strength = calc_signal_strength(cycle, X, signal_strength)
    match line:
        case [noop]:
            pass
        case ['addx', val]:
            cycle += 1
            signal_strength = calc_signal_strength(cycle, X, signal_strength)
            X += int(val)

# Part 1
print(signal_strength)


# Part 2
class Sprite:
    def __init__(self, pos=1):
        self.pos = pos
       
    @property
    def pos(self):
        return self.area[1]
    
    @pos.setter
    def pos(self, x):
        self.area = [x-1, x, x+1]


class Crt:
    def __init__(self, width=40):
        self.cycle = 0
        self.width = width
        self.content = ''        

    def increment_cycle(self):
        self.cycle += 1
        if self.pos() == 0:
            self.content += '\n'

    def pos(self):
        return self.cycle % self.width


sprite = Sprite()
crt = Crt()
crt.content += '#' if crt.pos() in sprite.area else '.'

for line in program:
    crt.increment_cycle()
    crt.content += '#' if crt.pos() in sprite.area else '.'

    match line:
        case [noop]:
            pass
        case ['addx', val]:
            crt.increment_cycle()            
            sprite.pos += int(val)
            crt.content += '#' if crt.pos() in sprite.area else '.'

print(crt.content)