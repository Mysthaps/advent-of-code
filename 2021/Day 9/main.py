with open("input.txt") as f:
    f = f.read().split()
    f = [list(i) for i in f]
    f = [[int(j) for j in i] for i in f]

# Part One

risk = 0
for i in range(len(f)):
    for j in range(len(f[i])):
        neighbors = []
        if i - 1 >= 0:
            neighbors.append(f[i-1][j])
        if i + 1 < len(f):
            neighbors.append(f[i+1][j])
        if j - 1 >= 0:
            neighbors.append(f[i][j-1])
        if j + 1 < len(f[i]):
            neighbors.append(f[i][j+1])
        isLow = True
        for k in range(len(neighbors)):
            if f[i][j] >= neighbors[k]:
                isLow = False
        if isLow:
            risk += f[i][j] + 1

print(risk)

# Part Two, rechecking Low Points because why not

def checkNeighbors(i, j, neighbors = []):
    print([i-1, j] in neighbors, [i-1, j] in neighbors == False)
    if i - 1 >= 0 and [i-1, j] in neighbors == False:
        neighbors.append([i-1, j])
    if i + 1 < len(f) and [i+1, j] in neighbors == False:
        neighbors.append([i+1, j])
    if j - 1 >= 0 and [i, j-1] in neighbors == False:
        neighbors.append([i, j-1])
    if j + 1 < len(f[i]) and [i, j+1] in neighbors == False:
        neighbors.append([i, j+1])
    return neighbors

largests = [0, 0, 0]
for i in range(len(f)):
    for j in range(len(f[i])):
        neighbors = checkNeighbors(i, j)

print(largests)