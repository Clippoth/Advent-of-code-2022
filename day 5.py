from copy import deepcopy
import re

with open('day 5 input.txt') as fin:
    input = list(fin.read().split('\n\n'))

def prepare(input):
    data = deepcopy(input)
    rows = data[0].split('\n')
    positions = rows[len(rows) - 1]

    last_position = int(positions[len(positions) - 2])

    columns = {}

    for position in range(1, last_position+1):
        position_index = positions.index(str(position))

        columns[position] = []

        for x in range(0, len(rows)-1):
            crate = rows[x][position_index]
            if crate != ' ':
                columns[position].append(crate)
        columns[position].reverse()

        steps = list(map(lambda x: re.findall(r'\d+', x), data[1].split('\n')))
 
    return [columns, steps]

def popelement(arr, fromPos, toPos, n = 1):
    if n > 1:
        items = arr[fromPos][-n:]
        del arr[fromPos][len(arr[fromPos]) - n:]
        arr[toPos].extend(items)
    else:
        item = arr[fromPos].pop()
        arr[toPos].append(item)

def part1():
    columns, steps = prepare(input)

    for step in steps:
        items = int(step[0])
        fromPos = int(step[1])
        toPos = int(step[2])

        for x in range(0, items):
            popelement(columns, fromPos, toPos)

    return ''.join([values.pop() for keys, values in columns.items()])

def part2():
    columns, steps = prepare(input)

    for step in steps:
        count = int(step[0])
        fromPos = int(step[1])
        toPos = int(step[2])

        
        popelement(columns, fromPos, toPos, count)

    return ''.join([values.pop() for keys, values in columns.items()])


print('Answer to part 1 is: ', part1())
print('Answer to part 2 is: ', part2())