with open("input.txt") as f:
    f = f.read().split()

p1pos = int(f[4])
p2pos = int(f[9])

p1score = 0
p2score = 0
rolls = 0

# Part One

i = 0

def the():
    global i
    i = (i % 100) + 1
    return i

while p1score < 1000 and p2score < 1000:
    p1pos = (p1pos + the() + the() + the()) % 10
    if p1pos == 0:
        p1score += 10
    else:
        p1score += p1pos
    rolls += 3
    if p1score >= 1000:
        print(p2score * rolls)
        break

    p2pos = (p2pos + the() + the() + the()) % 10
    if p2pos == 0:
        p2score += 10
    else:
        p2score += p2pos
    rolls += 3
    if p2score >= 1000:
        print(p1score * rolls)
        break

# Part Two

p1pos = int(f[4])
p2pos = int(f[9])

p1score = 0
p2score = 0
rolls = 0

