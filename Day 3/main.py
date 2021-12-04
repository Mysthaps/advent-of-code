with open("input.txt") as f:
    f = f.read().split("\n")

# Part One

for i in range(len(f)):
    f[i] = list(f[i])
half = -(-len(f)//2)

gamma = ""
epsilon = ""
for i in range(len(f[0])):
    amount = 0
    for j in range(len(f)):
        if f[j][i] == "1":
            amount += 1
    if amount >= half:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(int(gamma, 2)*int(epsilon, 2))

# Part Two, god this is really fucking scuffed and I'm not going to clean it up
i = 0
while i <= len(f[0]):
    amount = 0
    for j in range(len(f)):
        if f[j][i] == "1":
            amount += 1
    j = 0
    half = -(-len(f)//2)
    while j < len(f):
        if (amount >= half and f[j][i] == "0") or (amount < half and f[j][i] == "1"):
            f.pop(j)
        else:
            j += 1
    if len(f) == 1:
        break
    i += 1
oxygen = ''.join(f[0])

with open("input.txt") as f:
    f = f.read().split("\n")

for i in range(len(f)):
    f[i] = list(f[i])

i = 0
while i <= len(f[0]):
    amount = 0
    for j in range(len(f)):
        if f[j][i] == "1":
            amount += 1
    j = 0
    half = -(-len(f)//2)
    while j < len(f):
        if (amount < half and f[j][i] == "0") or (amount >= half and f[j][i] == "1"):
            f.pop(j)
        else:
            j += 1
    if len(f) == 1:
        break
    i += 1
co2 = ''.join(f[0])

print(int(oxygen, 2)*int(co2, 2))
  