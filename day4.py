import utils

puzzle_input = utils.read_input('day4')


# part 1
count = 0
for line in puzzle_input.splitlines():
    first, second = line.split(',')
    f1l, f1h = first.split('-')
    s1l, s1h = second.split('-')

    if int(f1l) <= int(s1l) and int(s1h) <= int(f1h):
        # print('1', line)
        count +=1
    elif int(s1l) <= int(f1l) and int(f1h) <= int(s1h):
        # print('2', line)
        count +=1

print(count)


# part 2
overlaps = 0
for line in puzzle_input.splitlines():
    first, second = line.split(',')
    f1l, f1h = first.split('-')
    s1l, s1h = second.split('-')

    r1 = range(int(f1l), int(f1h) + 1)
    r2 = range(int(s1l), int(s1h) + 1)

    if (r1.start in r2) or (r1.stop - 1 in r2) or (r2.start in r1) or (r2.stop - 1 in r1):
        print(line)
        overlaps += 1


print(overlaps)
