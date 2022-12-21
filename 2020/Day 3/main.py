with open("input.txt") as f:
    f = list(map(str, f.read().split("\n")))
    f = [list(i) for i in f]

# Part One

x = 3
y = 1

n = 0
while y < len(f):
    if x >= len(f[y]):
        x -= len(f[y])
    if f[y][x] == "#":
        n += 1
    x += 3
    y += 1

print(n)

# Part Two

s = 1

x = 1
y = 1

n = 0
while y < len(f):
    if x >= len(f[y]):
        x -= len(f[y])
    if f[y][x] == "#":
        n += 1
    x += 1
    y += 1

s *= n

x = 3
y = 1

n = 0
while y < len(f):
    if x >= len(f[y]):
        x -= len(f[y])
    if f[y][x] == "#":
        n += 1
    x += 3
    y += 1

s *= n

x = 5
y = 1

n = 0
while y < len(f):
    if x >= len(f[y]):
        x -= len(f[y])
    if f[y][x] == "#":
        n += 1
    x += 5
    y += 1

s *= n

x = 7
y = 1

n = 0
while y < len(f):
    if x >= len(f[y]):
        x -= len(f[y])
    if f[y][x] == "#":
        n += 1
    x += 7
    y += 1

s *= n

x = 1
y = 2

n = 0
while y < len(f):
    if x >= len(f[y]):
        x -= len(f[y])
    if f[y][x] == "#":
        n += 1
    x += 1
    y += 2

s *= n
print(s)