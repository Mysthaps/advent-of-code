with open("input.txt") as f:
    f = list(map(str, f.read().split("\n")))

# Part One

l = []
for i in f:
    rl = 0
    ru = 127

    cl = 0
    cu = 7

    for j in range(len(i)):
        if i[j] == "F":
            if j == 6:
                r = rl
            else:
                ru = (ru + rl) // 2
        elif i[j] == "B":
            if j == 6:
                r = ru
            else:
                rl = round((ru + rl) / 2)

        if i[j] == "L":
            if j == 9:
                c = cl
            else:
                cu = (cu + cl) // 2
        elif i[j] == "R":
            if j == 9:
                c = cu
            else:
                cl = round((cu + cl) / 2)
    
    l.append(r * 8 + c)

print(max(l))

# Part Two

l.sort()
a = l[0]
i = 0
while True:
    if l[i] == a:
        a += 1
        i += 1
    else:
        print(a)
        break