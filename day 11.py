import sys
with open("day 11 input.txt", encoding='utf8') as fin:
    #data = fin.read().split("\n\n")
    index = 0
    monkeys = []
    while True:
        #monkey number
        line = fin.readline()
        if line == "":
            break
        index = int(line.split()[1][:-1]) 
        monkeys.append({"count": index})
        # Items
        line = fin.readline()
        numbers = line.split(":")[1]
        numbers = list(map(int, numbers.split(",")))
        monkeys[index]["items"] = numbers
        # Operation
        line = fin.readline().split("=")[1].split() # line = [old, +*, number]
        monkeys[index]["operation"] = [line[1], line[2]] # operation contains the operand and the number
        # Test
        monkeys[index]["test"] = fin.readline().split("by")[1] # put the test number in Test
        # True
        monkeys[index]["true"] = fin.readline().split("monkey")[1] # destination monkey number if True
        # Falsee
        monkeys[index]["false"] = fin.readline().split("monkey")[1] # Destination monkey number if False
        #blank
        fin.readline().strip()
# least common multiple
lcm = 1
for monkey in monkeys:
    lcm *= int(monkey["test"])
print(lcm)

#part 1
#n_turni = 20

#part 2
n_turni = 10000

monkey_business = [0 for i in range(8)]

for _ in range(n_turni):
    for monkey in monkeys:
        while len(monkey["items"]) > 0:
            item = monkey["items"].pop(0)
            monkey_business[monkey["count"]] += 1
            if monkey["operation"][0] == '*':
                if monkey["operation"][1] == 'old':
                    item *= item
                else:
                    item *= int(monkey["operation"][1])
            else:
                item += int(monkey["operation"][1])
            
            if n_turni == 20:
                item = round(item//3)
            modulo = int(monkey["test"])
            item %= lcm
            reminder = item % modulo == 0
        
            if reminder:
                sendTo = int(monkey["true"])
            else:
                sendTo = int(monkey["false"])
            monkeys[sendTo]["items"].append(item)

monkey_business.sort(reverse=True)
print(monkey_business[0]*monkey_business[1])