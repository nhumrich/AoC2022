import utils
from collections import defaultdict

puzzle_input = utils.read_input('day6')

def part_one(line):
    for i, char in enumerate(line):
        if i < 3:
            continue
        characters = line[i-4:i]
        if len(set(characters)) == 4:
            print(i)
            return


def part_two(line):
    for i, char in enumerate(line):
        if i < 14:
            continue
        characters = line[i - 14:i]
        if len(set(characters)) == 14:
            print(i)
            return

for line in puzzle_input.splitlines():
    # part_one(line)
    part_two(line)

