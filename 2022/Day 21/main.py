with open("input.txt") as f:
    f = f.read().split("\n")
    f = [i.split(" ") for i in f]

monkeys = {}

def math(a, op, b):
    if op == "+": return a+b
    if op == "-": return a-b
    if op == "*": return a*b
    return int(a/b)

for i in f:
    monkeys[i[0][0:4]] = -999

while monkeys["root"] == -999:
    for i in f:
        if i[1].isdigit():
            monkeys[i[0][0:4]] = int(i[1])
        else:
            if monkeys[i[1]] != -999 and monkeys[i[3]] != -999:
                monkeys[i[0][0:4]] = math(monkeys[i[1]], i[2], monkeys[i[3]])

print(monkeys["root"])

monkeys = {}
for i in f:
    monkeys[i[0][0:4]] = -999

while True:
    changed = False
    for i in f:
        if monkeys[i[0][0:4]] == -999:
            if i[1].isdigit() and i[0] != "humn:":
                monkeys[i[0][0:4]] = int(i[1])
                changed = True
    ##        else:
    ##            if monkeys[i[1]] != -999 and monkeys[i[3]] != -999 and i[1] != "humn" and i[3] != "humn":
    ##                monkeys[i[0][0:4]] = math(monkeys[i[1]], i[2], monkeys[i[3]])
    ##                changed = True
    if changed == False:
        break

print(monkeys)
