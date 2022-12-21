with open("input.txt") as f:
    f = f.read().split("\n")
    f = [i.split(",") for i in f]
    f = [[j.split("-") for j in i] for i in f]
    f = [[[int(k) for k in j] for j in i] for i in f]

p1 = 0
p2 = 0
for i in range(len(f)):
    if (f[i][0][0] >= f[i][1][0] and f[i][0][1] <= f[i][1][1]) or (f[i][0][0] <= f[i][1][0] and f[i][0][1] >= f[i][1][1]):
        p1 += 1
    if (f[i][1][0] <= f[i][0][0] <= f[i][1][1]) or (f[i][0][0] <= f[i][1][0] <= f[i][0][1]):
        p2 += 1

print(p1)
print(p2)