with open("input.txt") as f:
    f = f.read().split("\n")
    f = [list(i) for i in f]
    f = [[int(j) for j in i] for i in f]

shines = 0

def shine(i, j):
    global shines
    for d in range(-1, 2):
        x = i + d
        if x > -1 and x < len(f):
            for e in range(-1, 2):
                y = j + e
                if y > -1 and y < len(f[i]):
                    if f[x][y] != 0:
                        f[x][y] += 1
                        if f[x][y] > 9:
                            shines += 1
                            f[x][y] = 0
                            f_ = [[str(j) for j in i] for i in f]
                            f_ = ["".join(i) for i in f_]
                            for i in range(len(f_)):
                                print(f_[i])
                            shine(x, y)

for step in range(2):
    for i in range(len(f)):
        for j in range(len(f[i])):
            f[i][j] += 1
            if f[i][j] > 9:
                shines += 1
                shine(i, j)
                

print(shines)