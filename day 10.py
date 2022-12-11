with open("day 10 input.txt") as f:
    instructions = [x.split() for x in f]

def part1():
    signalStrenghts = []
    clk = 0
    regX = 1
    for row in range(1, len(instructions)):
        if instructions[row-1][0] == 'noop':
            clk += 1
            if checkClk(clk):
                signalStrenghts.append(clk*regX)
        else:
            for _ in range(2):
                clk += 1
                if checkClk(clk):
                    signalStrenghts.append(clk*regX)
            regX += int(instructions[row-1][1])
    return sum(signalStrenghts), max
            
def checkClk(clk):
    check = False
    if clk==20 or clk==60 or clk==100 or clk==140 or clk==180 or clk==220:
        check = True
    return check
def update_pixel(reg, cycle, pixel):
    #draw a # only if the range (X-1, X+1) contains the position where the CRT is currently drawing
    # the position where the CRT is drawing must be normalized by 40, since the sprite is always in the 1st row
    pos = (cycle - 1) % 40
    if pos in {reg-1, reg, reg+1}:
        pixel[cycle - 1] = '#'

pixels = list("." * 40 * 6)
def part2():
    clk = 0
    cycle = 0
    reg = 1
    for row in range(0, len(instructions)):
        if instructions[row][0] == "noop":
            cycle += 1
            update_pixel(reg, cycle, pixels)
        else:
            cycle += 1
            update_pixel(reg, cycle, pixels)
            cycle += 1
            update_pixel(reg, cycle, pixels)
            reg += int(instructions[row][1])
    for row in range(0,201,40):
        print("".join(pixels[row:row +40]))


print("Answer to part 1 is:", part1())
print("Answer to part 2 is written here below!")
part2()


