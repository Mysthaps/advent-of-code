with open("input.txt") as f:
    f = f.read().split("\n")
    f = [i.split(" ") for i in f]

# Part One

check = [0] * len(f)
i = 0
acc = 0

while i < len(f):
    if check[i] == 1:
        break
    check[i] = 1
    if f[i][0] == "nop":
        i += 1
    elif f[i][0] == "acc":
        acc += int(f[i][1])
        i += 1
    elif f[i][0] == "jmp":
        i += int(f[i][1])

print(acc)

# Part Two

check = [0] * len(f)
i = 0
acc = 0

while i < len(f):
    if check[i] == 1:
        break
    check[i] = 1
    if f[i][0] == "nop":
        i += 1
    elif f[i][0] == "acc":
        acc += int(f[i][1])
        i += 1
    elif f[i][0] == "jmp":
        i += int(f[i][1])

print(acc)