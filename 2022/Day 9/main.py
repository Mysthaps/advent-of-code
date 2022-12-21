with open("input.txt") as f:
    f = f.read().split("\n")
    f = [i.split(" ") for i in f]

c = []

for i in range(1000):
    c.append([])
    for j in range(1000):
        c[i].append(False)

head = [500, 500]
tail = [500, 500]

def move(direc):
    if direc == "U" or direc == "R":
        return 1
    return -1

for cmd in f:
    direc = cmd[0]
    amt = int(cmd[1])

    for i in range(amt):
        if direc == "U" or direc == "D":
            head[0] += move(direc)
        if direc == "L" or direc == "R":
            head[1] += move(direc)

        if abs(tail[0] - head[0]) > 1 or abs(tail[1] - head[1]) > 1:
            if direc == "U" or direc == "D":
                tail[0] += move(direc)
            if direc == "L" or direc == "R":
                tail[1] += move(direc)

            if abs(tail[0] - head[0]) == 1 and abs(tail[1] - head[1]) == 1:
                if direc == "U" or direc == "D":
                    tail[1] = head[1]
                if direc == "L" or direc == "R":
                    tail[0] = head[0]

        c[tail[0]][tail[1]] = True

p1 = 0
for i in c:
    for j in i:
        if j == True:
            p1 += 1
print(p1)
