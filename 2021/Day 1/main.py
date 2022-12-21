with open("input.txt") as f:
    f = f.read().split("\n")

for i in range(len(f)):
    f[i] = int(f[i])

count = 0
prev = f[0] + f[1] + f[2]
cur = 0
for i in range(3, len(f)):
    cur = f[i] + f[i-1] + f[i-2]
    if cur > prev:
        count = count + 1
    prev = cur

print(count)
