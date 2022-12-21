with open("input.txt") as f:
    f = f.read().split("\n")
    for i in range(len(f)):
        f[i] = f[i].split(" -> ")
        for j in range(len(f[i])):
            f[i][j] = f[i][j].split(",")

a = []
for i in range(1000):
    a.append([])
    for j in range(1000):
        a[i].append(0)

# Part One

for i in range(len(f)):
    x1 = int(f[i][0][0])
    y1 = int(f[i][0][1])
    x2 = int(f[i][1][0])
    y2 = int(f[i][1][1])
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            a[y][x1] += 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            a[y1][x] += 1

intersections = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] > 1:
            intersections += 1

print(intersections)

# Part Two

for i in range(len(f)):
    x1 = int(f[i][0][0])
    x2 = int(f[i][1][0])
    y1 = int(f[i][0][1])
    y2 = int(f[i][1][1])
    if x1 != x2 and y1 != y2:
        y = y1
        if x1 < x2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                a[y][x] += 1
                if y1 < y2:
                    y += 1
                else: 
                    y -= 1
        else: 
            for x in range(max(x1, x2), min(x1, x2) - 1, -1):
                a[y][x] += 1
                if y1 < y2:
                    y += 1
                else: 
                    y -= 1

intersections = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] > 1:
            intersections += 1

print(intersections)