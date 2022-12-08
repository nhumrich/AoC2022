import utils
from collections import defaultdict
from dataclasses import dataclass, field

puzzle_input = utils.read_input('day7')

@dataclass
class Directory:
    name: str
    parent: 'Directory|None' = None
    size: int = 0
    files: set[str] = field(default_factory=set)

    def get_name(self):
        if not self.parent:
            return self.name
        return f'{self.parent.get_name()}/{self.name}'
    def __str__(self):
        return f'{self.get_name()} - {self.size=}'


    def add_to_size(self, size):
        self.size += size
        if self.parent:
            self.parent.add_to_size(size)

    def add_file(self, size, name):
        if name not in self.files:
            self.files.add(name)

        self.add_to_size(size)

def part_one():
    max_size = 100_000
    root_directory = Directory(name='/')
    current_directory = root_directory
    all_directories = [current_directory]
    lines = iter(puzzle_input.splitlines())
    while line:= next(lines, False):
        match line.split():
            case ['$', 'cd', '/']:
                current_directory = root_directory
            case ['$', 'cd', '..']:
                current_directory = current_directory.parent
            case ['$', 'cd', dir]:
                subdir = Directory(name=dir, parent=current_directory)
                all_directories.append(subdir)
                current_directory = subdir
            case ['$', 'ls']:
                pass
            case ['dir', dir]:
                pass
            case [size, filename]:
                current_directory.add_file(int(size), filename)


    sum_so_far = 0
    for dir in all_directories:
        if dir.size <= max_size:
            sum_so_far += dir.size
    print(sum_so_far)



def part_two():
    available_size = 70_000_000
    needed_space = 30_000_000
    root_directory = Directory(name='/')
    current_directory = root_directory
    all_directories = [current_directory]
    lines = iter(puzzle_input.splitlines())
    while line := next(lines, False):
        match line.split():
            case ['$', 'cd', '/']:
                current_directory = root_directory
            case ['$', 'cd', '..']:
                current_directory = current_directory.parent
            case ['$', 'cd', dir]:
                subdir = Directory(name=dir, parent=current_directory)
                all_directories.append(subdir)
                current_directory = subdir
            case ['$', 'ls']:
                pass
            case ['dir', dir]:
                pass
            case [size, filename]:
                current_directory.add_file(int(size), filename)

    sum_so_far = 0
    current_free = available_size - root_directory.size
    amount_to_free = needed_space - current_free
    for dir in sorted(all_directories, key=lambda d: d.size):
        if dir.size >= amount_to_free:
            print(dir)
            return



part_one()
part_two()
