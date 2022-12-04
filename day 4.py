with open('day 4 input.txt') as fin:
    data = fin.read().split('\n')

allPairs = [[[int(i) for i in sec.split('-')] for sec in row.split(',')] for row in data]

def part1():
    pairs = allPairs
    i = 0
    counter = 0
    for pair in pairs:
        first = set(range(pair[0][0], pair[0][1]+1))
        second = set(range(pair[1][0], pair[1][1]+1))
        if first <= second:
            counter += 1
        elif second < first:
            counter += 1
        i += 1
    return counter

def part2():
    pairs = allPairs
    i = 0
    counter = 0
    for pair in pairs:
        first = set(range(pair[0][0], pair[0][1]+1))
        second = set(range(pair[1][0], pair[1][1]+1))
        if not first.isdisjoint(second):
            counter += 1
        i += 1
    return counter

print("Answer to part 1 is: ", part1())
print("Answer to part 2 is: ", part2())
