import utils
from collections import defaultdict
from dataclasses import dataclass, field
import itertools

puzzle_input = utils.read_input('day8', False)


tree_grid = []
# build grid
for line in puzzle_input.splitlines():
    tree_grid.append([int(char) for char in line])


def part_one():
    visible_trees = []
    for x, y in itertools.product(range(len(tree_grid)), range(len(tree_grid[0]))):
        is_visible = False
        current = tree_grid[x][y]
        # look above
        for i in reversed(range(0, x)):
            height = tree_grid[i][y]
            if height >= current:
                # not visible from this edge
                break
        else:
            is_visible = True

        # look below
        for i in range(x+1, len(tree_grid)):
            if tree_grid[i][y] >= current:
                break
        else:
            is_visible = True

        # look left
        for i in reversed(range(0, y)):
            if current <= tree_grid[x][i]:
                break
        else:
            is_visible = True

        # look right
        for i in range(y+1, len(tree_grid[0])):
            if current <= tree_grid[x][i]:
                break
        else:
            is_visible = True


        if is_visible:
            visible_trees.append((x,y,current))

    print(visible_trees)
    print(len(visible_trees))
def part_two():
    best_scenic_score = 0
    for x, y in itertools.product(range(len(tree_grid)), range(len(tree_grid[0]))):
        current = tree_grid[x][y]
        # look above
        trees_sceen_top = 0
        for i in reversed(range(0, x)):
            height = tree_grid[i][y]
            trees_sceen_top += 1
            if height >= current:
                # not visible from this edge
                break

        # look below
        trees_seen_below = 0
        for i in range(x + 1, len(tree_grid)):
            trees_seen_below += 1
            if tree_grid[i][y] >= current:
                break

        # look left
        trees_seen_left = 0
        for i in reversed(range(0, y)):
            trees_seen_left += 1
            if current <= tree_grid[x][i]:
                break

        # look right
        trees_seen_right = 0
        for i in range(y + 1, len(tree_grid[0])):
            trees_seen_right += 1
            if current <= tree_grid[x][i]:
                break

        scenic_score = trees_seen_right * trees_seen_left * trees_sceen_top * trees_seen_below
        if scenic_score > best_scenic_score:
            best_scenic_score = scenic_score

    print(best_scenic_score)


part_one()
part_two()
