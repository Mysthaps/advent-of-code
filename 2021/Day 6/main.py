with open("input.txt") as f:
    f = f.read().split(",")
    
for i in range(len(f)):
    f[i] = int(f[i])

# Part One

for something in range(80):
    for i in range(len(f)):
        if f[i] == 0:
            f[i] = 7
            f.append(8)
        f[i] -= 1
print(len(f))

# Part Two, but a different method

with open("input.txt") as f:
    f = f.read().split(",")
    
for i in range(len(f)):
    f[i] = int(f[i])

sets = []
for something in range(9):
    sets.append(0)

for i in range(len(f)):
    sets[f[i]] += 1

for something in range(256):
    old = sets[0]
    sets[0] = sets[1]
    sets[1] = sets[2]
    sets[2] = sets[3]
    sets[3] = sets[4]
    sets[4] = sets[5]
    sets[5] = sets[6]
    sets[6] = sets[7]
    sets[7] = sets[8]
    sets[8] = old
    sets[6] += old

total = 0
for i in range(len(sets)):
    total += sets[i]

print(total)