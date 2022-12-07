# Advent of Code 2022
#
# From https://adventofcode.com/2022/day/7
#


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.contents = []

    def __repr__(self):
        return f"Directory: {self.name}"

    @property
    def size(self):
        return sum(item.size for item in self.contents)


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)

    def __repr__(self):
        return f"File: {self.name}"


data = open(f'../inputs/day7.txt', 'r').read().split('\n')
root_directory = Directory('root', None)
wd = None
directories = []

for cmd in data:
    if '$ cd' in cmd:
        dir_ = cmd.split(' ')[-1]
        if dir_ == '/':
            wd = root_directory
            continue
        elif dir_ == '..':
            wd = wd.parent
            continue
        else:
            for item_ in wd.contents:
                if isinstance(item_, Directory) and item_.name == dir_:
                    wd = item_
                    break
            if wd.name == dir_:
                continue
        print(f"Error: In directory {wd.name}, unable to complete command {cmd}")
        raise Exception
    elif '$ ls' in cmd:
        continue
    else:
        size_or_dir, name_ = cmd.split(' ')
        if size_or_dir.isnumeric():
            file = File(name_, size_or_dir)
            wd.contents.append(file)
        else:
            directory = Directory(name_, wd)
            wd.contents.append(directory)
            directories.append(directory)

print(f'Day 7, Part 1 {sum(directory.size for directory in directories if directory.size <= 100000)}')

disk_size = 70000000
required = 30000000
used = root_directory.size
needed_to_free = required - (disk_size - used)
print(f'Day 7, Part 2 {min(directory.size for directory in directories if directory.size >= needed_to_free)}')
