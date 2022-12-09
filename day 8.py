with open("day 8 input.txt") as fin:
    forest = [[int(i) for i in line.strip()] for line in fin.read().splitlines()]

#allora il problema è che verso il bordo conta giusto, mentre verso il centro conta uno in meno

def vertical_vector(i, j):
    vectorUp = []
    vectorDown = []
    for x in range(i):
        vectorUp.append(forest[x][j])
    for x in range(i+1, len(forest)):
        vectorDown.append(forest[x][j])
    return vectorUp, vectorDown

def visible(i, j, height):
    yes = False
  
    vectorUp, vectorDown = vertical_vector(i,j)
    if max(forest[i][j+1:]) < height:
        yes = True
    elif max(forest[i][:j]) < height:
        yes = True
    elif max(vectorUp) < height or max(vectorDown) < height:
        yes = True
    return yes

def vectors(i,j, height):
    if height==5:
        pass
    vectorUp = []
    vectorDown = []
    vectorRight = []
    vectorLeft = []
    for x in range(i):
        vectorUp.append(forest[x][j])
    vectorUp.reverse()
    for x in range(i+1, len(forest)):
        vectorDown.append(forest[x][j])
    for x in range(j):
        vectorLeft.append(forest[i][x])
    vectorLeft.reverse()
    for x in range(j+1, len(forest)):
        vectorRight.append(forest[i][x])
    
    return vectorUp, vectorDown, vectorLeft, vectorRight
    
def scorecalc(up, down, left, right, height):
    cup = 0
    cdown = 0
    cleft = 0
    cright = 0
    score = 0
    for x in up:
        cup += 1
        if x >= height:
            break
    for x in down:
        cdown +=1
        if x>= height:
            break
    for x in left:
        cleft +=1
        if x >= height:
            break
    for x in right:
        cright += 1
        if x >= height:
            break
    score = cup*cdown*cleft*cright
    return score

def part1():
    counter = 2*(len(forest)-2) + 2*len(forest)
    for row in range(1, len(forest)-1):
        for column in range(1, len(forest)-1):
            if column == 0 or column == len(forest) or row == 0 or row == len(forest):
                pass
            else:
                height = forest[row][column]
                if visible(row, column, height):
                    counter += 1
    return counter

def part2():
    score = 0
    iconicScore = 0
    for row in range(1, len(forest)-1):
        for column in range(1, len(forest)-1):
            if column == 0 or column == len(forest)-1 or row == 0 or row == len(forest)-1:
                pass
            else:
                height = forest[row][column]
                vup, vdown, vleft, vright = vectors(row,column, height)
                iconicScore = scorecalc(vup,vdown,vleft,vright, height)
                if iconicScore > score:
                    score = iconicScore 
    return score

print("Answer to part 1 is: ", part1())
print("Answer to part 2 is: ", part2())



