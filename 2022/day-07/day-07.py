with open('2022/day-07/input.txt') as f:
    output = [x.strip() for x in f.read().split('$')[1:]]


class file:
    def __init__(self, name, parent=None, size=0, is_folder=True):
        self.name = name
        self.is_folder = is_folder
        self.size_ = size
        self.parent = parent
        if self.parent:
            self.parent.children.append(self)
            self.level = self.parent.level + 1
        else:
            self.level = 0
        self.children = []

    def size(self):
        if self.is_folder:
            return sum([child.size() for child in self.children])
        return self.size_

    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        else:
            None
            
    def __str__(self):
        base = f"{self.level * '  '}- {self.name} ({'dir' if self.is_folder else 'file'}, size={self.size()}')"
        for child in self.children:
            base += f'\n{child}'
        return base
 
           
all_dirs = []
root = file('/')
all_dirs.append(root)
for step in output:
    command, *results = step.split('\n')
    if command.startswith('cd'):
        if command[3:] == '/':
            current_dir = root
        elif command[3:] == '..':
            current_dir = current_dir.parent
        else:
            current_dir = current_dir.get_child(command[3:])       
    elif command == 'ls':
        for result in results:
            first, second = result.split()
            if first == 'dir':
                dir_name = second
                if not current_dir.get_child(dir_name):
                    new_dir = file(dir_name, parent=current_dir)
                    all_dirs.append(new_dir)
            else:
                new_file = file(second, parent=current_dir, size=int(first), is_folder=False)

# Part 1
max_size = 100_000
print(sum(dir.size() for dir in all_dirs if dir.size() <= max_size))

# Par 2
total_size = 70_000_000
required_space = 30_000_000
current_space = total_size - root.size()
min_size = required_space - current_space
print(min([dir.size() for dir in all_dirs if dir.size() >= min_size]))

print(root)