with open("input.txt") as f:
    f = f.read().split("\n")
    f = [[int(j) for j in i.split(" ")] for i in f]

### Part 1 ###
part_1 = 0
check = []

def recursion_1(total, i, idx):
    global part_1
    if total > f[i][0]:
        return
    
    if idx == len(f[i]):
        if total == f[i][0] and not check[i]:
            part_1 += f[i][0]
            check[i] = True
        return
    
    recursion_1(total + f[i][idx], i, idx+1)
    recursion_1(total * f[i][idx], i, idx+1)

for i in range(len(f)):
    check.append(False)
    recursion_1(f[i][1], i, 2)

print("Part 1:", part_1)

### Part 2 ###
part_2 = 0
check = []

def recursion_2(total, i, idx):
    global part_2
    if total > f[i][0]:
        return
    
    if idx == len(f[i]):
        if total == f[i][0] and not check[i]:
            part_2 += f[i][0]
            check[i] = True
        return
    
    recursion_2(total + f[i][idx], i, idx+1)
    recursion_2(total * f[i][idx], i, idx+1)
    recursion_2(int(str(total) + str(f[i][idx])), i, idx+1)

for i in range(len(f)):
    check.append(False)
    recursion_2(f[i][1], i, 2)

print("Part 2:", part_2)