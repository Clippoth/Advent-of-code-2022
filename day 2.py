with open('day 2 input.txt') as fin:
    data = fin.read().splitlines()
    allRounds = [[i for i in round.split(' ')] for round in data]


def won(round):
    win = False
    if round[0] == 'A' and round[1] == 'Y':
        win = True
    elif round[0] == 'B' and round[1] == 'Z':
        win = True
    elif round[0] == 'C' and round[1] == 'X':
        win = True
    return win

def draw(round):
    same = False
    if round[0] == 'A' and round[1] == 'X':
        same = True
    elif round[0] == 'B' and round[1] == 'Y':
        same = True
    elif round[0] == 'C' and round[1] == 'Z':
        same = True
    return same

def scoreSymbol(round, score):
    if round[1] == 'X':
        score += 1
    elif round[1] == 'Y':
        score += 2
    elif round[1] == 'Z':
        score += 3
    return score

def replaceSymbol(round):
    if round[1] == 'Z':         # you have to win
        if round[0] == 'A':
            round[1] = 'Y'
        elif round[0] == 'B':
            round[1] == 'Z'
        else:
            round[1] = 'X'

    elif round[1] == 'Y':       # you have to draw
        if round[0] == 'A':
            round[1] = 'X'
        elif round[0] == 'B':
            round[1] == 'Y'
        else:
            round[1] = 'Z'

    elif round[1] == 'X':       # you have to lose
        if round[0] == 'A':
            round[1] = 'Z'
        elif round[0] == 'B':
            round[1] == 'X'
        else:
            round[1] = 'Y'


def part1():
    score = 0
    rounds = allRounds
    for round in rounds:
        score = scoreSymbol(round, score)
        if won(round):
            score += 6
        elif draw(round):
            score += 3
    return score

def part2():
    rounds = allRounds
    score = 0
    for round in rounds:
        replaceSymbol(round)
    for round in rounds:
        score = scoreSymbol(round, score)
        if won(round):
            score += 6
        elif draw(round):
            score += 3
    return score

print("Answer to part 1 is: ", part1())
print("Answer to part 2 is: ", part2())

