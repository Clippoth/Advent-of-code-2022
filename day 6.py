with open('day 6 input.txt') as fin:
    data = list(fin.read())
print(len(data))

def part1():
    for i in range(0, len(data)-2):
        group = set(data[i:i+4])
        if len(group) == 4: 
            index = i+4
            return index

def part2():
    for i in range(0, len(data)-12):
        group = set(data[i:i+14])
        if len(group) == 14:
            index = i+14
            return index

print("Answer to part 1 is: ", part1())
print("Anwser to part 2 is: ", part2())