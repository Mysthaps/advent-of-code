with open("input.txt") as f:
    f = f.read().split("\n")

p1 = 0
for i in range(len(f)):
    half = int(len(f[i])/2)
    for j in f[i][0:half]:
        if j in f[i][half:len(f[i])]:
            if j.islower():
                p1 += ord(j) - 96
            else:
                p1 += ord(j) - 64 + 26
            break

p2 = 0
for i in range(0, len(f), 3):
    for j in f[i]:
        if j in f[i+1] and j in f[i+2]:
            if j.islower():
                p2 += ord(j) - 96
            else:
                p2 += ord(j) - 64 + 26
            break
print(p1)
print(p2)
