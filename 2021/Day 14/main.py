from collections import Counter

with open("input.txt") as f:
    f = f.read().split("\n")

# Part One

a = list(f[0])
rules = []
for i in range(2, len(f)):
    rules.append(f[i].split(" -> "))

for step in range(10):
    b = list(a)
    inserts = 0
    for i in range(len(b)-1):
        for j in range(len(rules)):
            if "".join([b[i], b[i+1]]) == rules[j][0]:
                a.insert(i+1+inserts, rules[j][1])
                inserts += 1

print(Counter(a))

# Part Two