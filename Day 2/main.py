with open("input.txt") as f:
    f = f.read().split("\n")

for i in range(len(f)):
    f[i] = f[i].split(" ")

# Part One

x = 0
y = 0
for i in range(len(f)):
    if f[i][0] == "forward":
        x += int(f[i][1])
    elif f[i][0] == "up":
        y -= int(f[i][1])
    elif f[i][0] == "down":
        y += int(f[i][1])

print(x*y)

# Part Two

x = 0
y = 0
aim = 0
for i in range(len(f)):
    if f[i][0] == "forward":
        x += int(f[i][1])
        y += aim * int(f[i][1])
    elif f[i][0] == "up":
        aim -= int(f[i][1])
    elif f[i][0] == "down":
        aim += int(f[i][1])

print(x*y)
