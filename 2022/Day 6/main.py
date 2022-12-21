with open("input.txt") as f:
    f = f.read()

for i in range(len(f)):
    if len(set(f[i:i+4])) == 4:
        print(i+4)
        break
for i in range(len(f)):
    if len(set(f[i:i+14])) == 14:
        print(i+14)
        break
