import os

for day in range(1,26):
    try:
        os.mkdir(f'day{day}')
    except:
        # I already made some
        print('nope on day', day)
        continue

    with open(f'day{day}/solution.py', 'w') as f:
        f.write(f"""
import utils

puzzle_input = utils.read_input('day{day}', True)

def part_one():
    print('day{day}')


def part_two():
    pass


part_one()
part_two()

""")
    with open(f'day{day}/main.input', 'w') as f:
        f.write('')
    with open(f'day{day}/test.input', 'w') as f:
        f.write('')
