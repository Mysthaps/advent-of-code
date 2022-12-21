with open("input.txt") as f:
    f = list(map(str, f.read().split("\n\n")))
    f = [i.split('\n') for i in f]

# Part One
s = 0
for i in f:
    l = []
    for j in i:
        for k in j:
            if k not in l:
                l.append(k)
    s += len(l)

print(s)

# Part Two
s = 0
for i in f:
    for j in i:
        for k in j:
            pass