with open("input.txt") as f:
    f = f.read().split("\n")
    f = [list(i) for i in f]
    f = [[int(j) for j in i] for i in f]

p1 = 0
p2 = 0
for i in range(len(f)):
    for j in range(len(f[i])):
        checktop = True
        checkbottom = True
        checkleft = True
        checkright = True
        score = 1
        for x in range(i-1, -1, -1):
            if f[x][j] >= f[i][j]:
                checktop = False
                score *= i-x
                break
        for x in range(i+1, len(f)):
            if f[x][j] >= f[i][j]:
                checkbottom = False
                score *= x-i
                break
        for y in range(j-1, -1, -1):
            if f[i][y] >= f[i][j] and y != j:
                checkleft = False
                score *= j-y
                break
        for y in range(j+1, len(f[i])):
            if f[i][y] >= f[i][j] and y != j:
                checkright = False
                score *= y-j
                break
        if checktop or checkbottom or checkleft or checkright or i == 0 or j == 0:
            p1 += 1
        if checktop:
            score *= i
        if checkbottom:
            score *= len(f) - i - 1
        if checkleft:
            score *= j
        if checkright:
            score *= len(f[i]) - j - 1
        p2 = max(p2, score)

print(p1)
print(p2)
