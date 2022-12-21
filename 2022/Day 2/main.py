with open("input.txt") as f:
    f = f.read().split("\n")

f = [i.split(" ") for i in f]

p1s = 0
p2s = 0
for i in range(len(f)):
    p1s += ord(f[i][1]) - 87
    p1s += ((ord(f[i][1]) - 23) - ord(f[i][0])+1)%3*3

    if f[i][1] == "X":
        p2s += (ord(f[i][0]))%3+1
    elif f[i][1] == "Y":
        p2s += (ord(f[i][0])+1)%3+4
    else:
        p2s += (ord(f[i][0])-1)%3+7

print(p1s)
print(p2s)
