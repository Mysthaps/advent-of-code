# Part One

f = open("input.txt")

s = 0
while True:
    a = f.readline().split()
    a = [i.strip(":").split("-") for i in a]
    if a == []:
        break

    a[0][0] = int(a[0][0])
    a[0][1] = int(a[0][1])

    n = 0

    for i in a[2][0]:
        if i == a[1][0]:
            n += 1

    if n >= a[0][0] and n <= a[0][1]:
        s += 1

print(s)

# Part Two

f = open("input.txt")

s = 0
while True:
    a = f.readline().split()
    a = [i.strip(":").split("-") for i in a]
    if a == []:
        break

    i = int(a[0][0]) - 1
    j = int(a[0][1]) - 1

    if len(a[2][0]) > j:
        if (a[2][0][i] == a[1][0] or a[2][0][j] == a[1][0]) and ((a[2][0][i] == a[1][0] and a[2][0][j] == a[1][0]) == False):
            s += 1

print(s)