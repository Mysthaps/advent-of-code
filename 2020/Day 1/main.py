with open("input.txt") as f:
    f = list(map(int, f.read().split("\n")))

# Part One

for i in range(len(f)):
    for j in range(i, len(f)):
        if f[i] + f[j] == 2020:
            print(f[i] * f[j])
            break

# Part Two
for i in range(len(f)):
    for j in range(i, len(f)):
        for k in range(j, len(f)):
            if f[i] + f[j] + f[k] == 2020:
                print(f[i] * f[j] * f[k])