with open("input.txt") as f:
    f = f.read().split("\n")

s = 0
l = []

for i in range(len(f)):
    if f[i] == '':
        l.append(s)
        s = 0
        continue
        
    s += int(f[i])

l.sort(reverse=True)
print(l[0])
print(l[0]+l[1]+l[2])
