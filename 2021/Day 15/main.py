with open("input.txt") as f:
    a = []
    for i in f.readlines():
        a.append(list(map(int, list(i.strip("\n")))))

q = [(0, 0)]
direc = [(0, 1), (1, 0)]

val = []

def move(s):
    global q, val
    if len(q) > 0:
        m = q.pop(0)
        x1 = m[0]
        y1 = m[1]

        for i in direc:
            x2 = x1 + i[0]
            y2 = y1 + i[1]

            if (x2 >= 0 and x2 <= len(a)-1) and (y2 >= 0 and y2 <= len(a[0])-1):
                if x2 == len(a)-1 and y2 == len(a[0])-1:
                    val.append(s)
                    return
                else:
                    s += a[x2][y2]
                    q.append((x2, y2))
                    move(s)

# Part One

move(0)
print(min(val))