import utils

puzzle_input = utils.read_input('day1')

sums = []
for elf in puzzle_input.split('\n\n'):
    numbers = elf.strip().split()
    sums.append(sum(map(int, numbers)))

# part 1
print(max(sums))

# part 2
print(sum(sorted(sums, reverse=True)[:3]))
