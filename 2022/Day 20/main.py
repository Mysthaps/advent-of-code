with open("input.txt") as f:
    f = f.read().split("\n")
    for i in range(len(f)):
        f[i] = [int(f[i]), i]

l = f.copy()
p1 = 0
for i in f:
    idx = l.index(i)
    l.remove(i)
    idx = (idx + i[0]) % (len(f) - 1)
    if idx == 0: idx = len(f)
    l.insert(idx, i)

zidx = 0
for i in f:
    if i[0] == 0:
        zidx = l.index(i)

for t in [1000, 2000, 3000]:
    p1 += l[(zidx + t) % len(f)][0]
print(p1)

## Part Two

for i in range(len(f)):
    f[i][0] *= 811589153

l = f.copy()
p2 = 0
for _ in range(10):
    for i in f:
        idx = l.index(i)
        l.remove(i)
        idx = (idx + i[0]) % (len(f) - 1)
        if idx == 0: idx = len(f)
        l.insert(idx, i)

zidx = 0
for i in f:
    if i[0] == 0:
        zidx = l.index(i)

for t in [1000, 2000, 3000]:
    p2 += l[(zidx + t) % len(f)][0]
print(p2)