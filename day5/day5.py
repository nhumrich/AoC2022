import utils
from collections import defaultdict

puzzle_input = utils.read_input('day5')

# part 1
def part_one():
    initial, steps = puzzle_input.split('\n\n')
    number_of_stacks = int(initial[-1])
    # print(number_of_stacks)
    stacks = defaultdict(list)
    for line in reversed(initial.splitlines()[:-1]):
        # print(line)
        for i in range(number_of_stacks):
            if len(line) > 1 + 4*i:
                letter = line[1 + 4*i]
                if letter != ' ':
                    stacks[i+1].append(letter)


    for line in steps.splitlines():
        _, amount, _, stack_origin, _, stack_destination = line.split()
        for i in range(int(amount)):
            container_id = stacks[int(stack_origin)].pop()
            stacks[int(stack_destination)].append(container_id)


    answer = ''
    for i in range(number_of_stacks):
        answer += stacks[i+1][-1]

    print(answer)

part_one()

def part_two():
    initial, steps = puzzle_input.split('\n\n')
    number_of_stacks = int(initial[-1])
    # print(number_of_stacks)
    stacks = defaultdict(list)
    for line in reversed(initial.splitlines()[:-1]):
        # print(line)
        for i in range(number_of_stacks):
            if len(line) > 1 + 4 * i:
                letter = line[1 + 4 * i]
                if letter != ' ':
                    stacks[i + 1].append(letter)

    for line in steps.splitlines():
        _, amount, _, stack_origin, _, stack_destination = line.split()
        new_stack = []
        for i in range(int(amount)):
            container_id = stacks[int(stack_origin)].pop()
            new_stack.append(container_id)

        while new_stack:
            stacks[int(stack_destination)].append(new_stack.pop())

    answer = ''
    for i in range(number_of_stacks):
        answer += stacks[i + 1][-1]

    print(answer)


part_two()