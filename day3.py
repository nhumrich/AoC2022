import utils

puzzle_input = utils.read_input('day3')


# part 1
def find_dup(first, second):
    for char in first:
        if char in second:
            return char

dupes = []
for index, line in enumerate(puzzle_input.splitlines()):
    first, second = line[:len(line) // 2], line[len(line) // 2:]

    dupes.append(find_dup(first, second))

sum = 0
for letter in dupes:
    if letter.islower():
        val = ord(letter) - ord('a') + 1
    else:
        val = ord(letter) - ord('A') + 27
    print(f'{letter=} {val=}')
    sum += val

print(f'{sum=}')


def find_common(group_list):
    one, two, three = group_list
    one = set(one)
    two = set(two)
    three = set(three)

    result = one.intersection(two).intersection(three)
    return result.pop()


group_list = []
results = []
for line in puzzle_input.splitlines():
    if len(group_list) == 3:
        results.append(find_common(group_list))

        group_list = []
        # find common
    group_list.append(line)
results.append(find_common(group_list))

sum2 = 0
for letter in results:
    if letter.islower():
        val = ord(letter) - ord('a') + 1
    else:
        val = ord(letter) - ord('A') + 27
    print(f'{letter=} {val=}')
    sum2 += val

print(f'{sum2=}')
