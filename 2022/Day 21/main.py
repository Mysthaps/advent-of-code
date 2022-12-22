with open("input.txt") as f:
    f = f.read().split("\n")
    f = [i.split(" ") for i in f]

monkeys = {}

def math(a, op, b, rev):
    if (op == "+" and rev == False) or (op == "-" and rev == True): return a+b
    if (op == "-" and rev == False) or (op == "+" and rev == True): return a-b
    if (op == "*" and rev == False) or (op == "/" and rev == True): return a*b
    return int(a/b)

for i in f:
    monkeys[i[0][0:4]] = -999

while monkeys["root"] == -999:
    for i in f:
        if i[1].isdigit():
            monkeys[i[0][0:4]] = int(i[1])
        else:
            if monkeys[i[1]] != -999 and monkeys[i[3]] != -999:
                monkeys[i[0][0:4]] = math(monkeys[i[1]], i[2], monkeys[i[3]], False)

print(monkeys["root"])

monkeys = {}
for i in f:
    monkeys[i[0][0:4]] = -999

while True:
    changed = False
    for i in f:
        if monkeys[i[0][0:4]] == -999:
            if i[1].isdigit():
                if i[0] != "humn:":
                    monkeys[i[0][0:4]] = int(i[1])
                    changed = True
            else:
                if monkeys[i[1]] != -999 and monkeys[i[3]] != -999:
                    monkeys[i[0][0:4]] = math(monkeys[i[1]], i[2], monkeys[i[3]], False)
                    changed = True
    if changed == False:
        break

cur = "root"
while cur != "humn":
    for i in f:
        if i[0][0:4] == cur:
            print(cur, i[1], i[2], i[3], monkeys[i[1]], monkeys[i[3]], monkeys[cur])
            if cur == "root":
                if monkeys[i[1]] == -999:
                    monkeys[i[1]] = monkeys[i[3]]
                    cur = i[1]
                else:
                    monkeys[i[3]] = monkeys[i[1]]
                    cur = i[3]
            else:
                if monkeys[i[1]] == -999:
                    monkeys[i[1]] = math(monkeys[cur], i[2], monkeys[i[3]], True)
                    cur = i[1]
                else:
                    if i[2] == "/":
                        monkeys[i[3]] = int(monkeys[cur] / monkeys[i[1]])
                    elif i[2] == "-":
                        monkeys[i[3]] = monkeys[i[1]] - monkeys[cur]
                    else:
                        monkeys[i[3]] = math(monkeys[cur], i[2], monkeys[i[1]], True)
                    cur = i[3]
            break
print(monkeys["humn"])
