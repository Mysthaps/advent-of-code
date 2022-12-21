from math import floor, ceil

with open("input.txt") as f:
    f = f.read().split("\n")
    f = [i.split(" ") for i in f]

monkeys = [[], [], [], [], [], [], [], []]
operations = []
tests = []
targets = []
inspections = [0, 0, 0, 0, 0, 0, 0, 0]
mod = 1

def mult(a, b):
    a %= mod
    b %= mod
    q = ceil(a*b / mod)
    return (a*b - q*mod) % mod

monkey = -1
for i in f:
    if i[0] == "Monkey":
        monkey += 1
    if len(i) < 3: continue
    if i[2] == 'Starting':
        for j in range(4, len(i)):
            monkeys[monkey].append(int(i[j][0:2]))
    if len(i) < 6: continue
    if i[2] == "Operation:":
        if i[7] == "old":
            operations.append([i[6], i[7]])
            continue
        operations.append([i[6], int(i[7])])
    if i[2] == "Test:":
        tests.append(int(i[5]))
        mod *= tests[monkey]
    if i[5] == "true:":
        targets.append([int(i[9])])
    if i[5] == "false:":
        targets[monkey].append(int(i[9]))

print(monkeys)
print(operations)
print(tests)
print(targets)

for _ in range(10000):
    for i in range(0, 8):
        for j in range(len(monkeys[i])):
            inspections[i] += 1
            if operations[i][0] == "+":
                monkeys[i][j] += operations[i][1]
            else:
                if operations[i][1] == "old":
                    monkeys[i][j] = mult(monkeys[i][j], monkeys[i][j])
                else:
                    monkeys[i][j] = mult(monkeys[i][j], operations[i][1])
            # monkeys[i][j] = floor(monkeys[i][j] / 3) # part 1
            if monkeys[i][j] % tests[i] == 0:
                monkeys[targets[i][0]].append(monkeys[i][j])
            else:
                monkeys[targets[i][1]].append(monkeys[i][j])
        monkeys[i] = []

print(inspections)