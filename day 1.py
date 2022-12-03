with open('day 1 input.txt') as fin:
    data = fin.read()
    print(type(data))
allElves = [[int(cal) for cal in elf.split()] for elf in data.split("\n\n")]
summed = []
for elf in allElves:
    summed.append(sum(elf))
summedSorted = sorted(summed)
print("Answer 1 is: ", max(summedSorted))
print("Answer 2 is: ", sum(summedSorted[-3:]))