with open('day 4 input.txt') as fin:
    data = fin.read().split('\n')

allPairs = [[[int(i) for i in sec.split('-')] for sec in row.split(',')] for row in data]

def contained(pair):
    yes = False
    if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1] or pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
        yes = True
    return yes

def overlap(pair):
    yes = False
    if pair[0][0] >= pair[1][0] and pair[0][0] <= pair[1][1] or pair[0][1] >= pair[1][0] and pair[0][1] <= pair[1][1]:
        yes = True
    elif contained(pair):
        yes = True
    return yes

def part1():
    pairs = allPairs
    i = 0
    counter = 0
    while i < len(pairs):
        if contained(pairs[i]):
            counter += 1
        i += 1
    return counter

def part2():
    pairs = allPairs
    i = 0
    counter = 0
    while i < len(pairs):
        if overlap(pairs[i]):
            counter += 1
        i += 1
    return counter

print("Answer to part 1 is: ", part1())
print("Answer to part 2 is: ", part2())

        

        

