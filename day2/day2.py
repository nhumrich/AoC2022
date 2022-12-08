import utils

puzzle_input = utils.read_input('day2')

points = {
    'Y': 2,
    'X': 1,
    'Z': 3,
    'A': 1,
    'B': 2,
    'C': 3
}


games = puzzle_input.splitlines()

# part one
points = 0
for game in games:
    match game:
        case 'A X':
            points += 4
        case 'A Y':
            points += 8
        case 'A Z':
            points += 3
        case 'B X':
            points += 1
        case 'B Y':
            points += 5
        case 'B Z':
            points += 9
        case 'C X':
            points += 7
        case 'C Y':
            points += 2
        case 'C Z':
            points += 6

print(points)

# part 2
points2 = 0
for game in games:
    match game:
        # A = Rock
        # x = lose
        case 'A X':
            points2 += 3
        # y = draw
        case 'A Y':
            points2 += 4
        # z = win
        case 'A Z':
            points2 += 8
        # B = paper
        case 'B X':
            points2 += 1
        case 'B Y':
            points2 += 5
        case 'B Z':
            points2 += 9
        # C = Scissors
        case 'C X':
            points2 += 2
        case 'C Y':
            points2 += 6
        case 'C Z':
            points2 += 7

print(points2)

