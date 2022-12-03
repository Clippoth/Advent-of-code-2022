import sys

with open('day 3 input.txt') as fin:
    data = list(fin.read().split('\n'))
    allBags = [[str(i) for i in bags] for bags in data]

ord

def part1():
    total = 0
    for bag in allBags:
        n = len(bag)
        c1, c2 = set(bag[:n//2]), set(bag[n//2:])
        match = c1.intersection(c2)
        
        for elem in match:
            val = ord(elem)
            if val > 96:
                total += val -96
            elif val > 64:
                total += val -38
    return total


def part2():
    total = 0
    i = 0
    while i < len(allBags):
        c1, c2, c3 = set(allBags[i]), set(allBags[i+1]), set(allBags[i+2])
        match = c1.intersection(c2,c3)
        for elem in match:
            val = ord(elem)
            if val > 96:
                total += val -96
            elif val > 64:
                total += val -38
        i += 3
    return total


print("Answer to part 1 is: ", part1())
print("Answer to part 2 is: ", part2())