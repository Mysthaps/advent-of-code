import sys
sys.setrecursionlimit(100000)

with open("input.txt") as f:
    f = f.read().split("\n")
    f = [[*i] for i in f]

lst = []
start = []
end = []

for i in range(len(f)):
    lst.append([])
    for j in range(len(f[i])):
        lst[i].append(-1)
        if f[i][j] == "S":
            start = [i, j]
        if f[i][j] == "E":
            end = [i, j]

def floodfill(i, j, steps, check):
    if steps >= check[i][j] and check[i][j] != -1:
        return
    check[i][j] = steps
    cur = ord(f[i][j])
    if (f[i][j] == "E"):
        print(steps)
        return
    if j < len(f[0])-1 and ((ord(f[i][j+1]) <= ord(f[i][j]) and f[i][j+1] != "E") or (ord(f[i][j+1]) == ord(f[i][j])+1) or (f[i][j+1] == "E" and f[i][j] == "z") or f[i][j] == "S"):
        floodfill(i, j+1, steps+1, check)
    if j > 0 and ((ord(f[i][j-1]) <= ord(f[i][j]) and f[i][j-1] != "E") or (ord(f[i][j-1]) == ord(f[i][j])+1) or (f[i][j-1] == "E" and f[i][j] == "z") or f[i][j] == "S"):
        floodfill(i, j-1, steps+1, check)
    if i < len(f)-1 and ((ord(f[i+1][j]) <= ord(f[i][j]) and f[i+1][j] != "E") or (ord(f[i+1][j]) == ord(f[i][j])+1) or (f[i+1][j] == "E" and f[i][j] == "z") or f[i][j] == "S"):
        floodfill(i+1, j, steps+1, check)
    if i > 0 and ((ord(f[i-1][j]) <= ord(f[i][j]) and f[i-1][j] != "E") or (ord(f[i-1][j]) == ord(f[i][j])+1) or (f[i-1][j] == "E" and f[i][j] == "z") or f[i][j] == "S"):
        floodfill(i-1, j, steps+1, check)


floodfill(start[0], start[1], 0, lst)