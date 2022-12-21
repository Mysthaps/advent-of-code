with open("input.txt") as f:
    f = f.read().split("\n")
    f = [i.split(" ") for i in f]

cycle = 0
x = 1
p1 = 0
p2 = [[], [], [], [], [], [], [], [], []]

def cyclecheck(cycle, x):
    global p1
    global p2
    if cycle % 40 == 20:
        p1 += cycle * x
    if ((cycle-1) % 40) + 1 >= x and ((cycle-1) % 40) + 1 <= x+2:
        p2[(cycle-1)//40].append("#")
    else:
        p2[(cycle-1)//40].append(".")

for i in range(len(f)):
    cycle += 1
    cyclecheck(cycle, x)
    if f[i][0] == "noop":
        continue
    cycle += 1
    cyclecheck(cycle, x)
    x += int(f[i][1])


print(p1)
for i in p2:
    for j in i:
        print(j, end = "")
    print()
