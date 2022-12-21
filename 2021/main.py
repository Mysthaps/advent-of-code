with open("input.txt") as f:
    f = f.read().split("\n")
    f = [i.split() for i in f]
    f = [[j.split(",") for j in i] for i in f]

print(f)
print(f[0])
print(f[0][0])

# Part One

a = [[[]*101]*101]*101

for i in f:
    for j in range(len(i[0][1])):
        pass