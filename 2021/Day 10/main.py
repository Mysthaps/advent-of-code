from statistics import median

with open("input.txt") as f:
    f = f.read().split("\n")
    f = [list(i) for i in f]

openings = ["(", "<", "[", "{"]
illegal = []

# Part One

for i in range(len(f)):
    a = []
    for j in range(len(f[i])):
        closings = [")", ">", "]", "}"]
        if f[i][j] in openings:
            a.append(f[i][j])
        elif (f[i][j] == ")" and a[len(a)-1] == "(") or (f[i][j] == "]" and a[len(a)-1] == "[") or (f[i][j] == ">" and a[len(a)-1] == "<") or (f[i][j] == "}" and a[len(a)-1] == "{"):
            a.pop(len(a)-1)
        else:
            illegal.append(f[i][j])
            break
score = 0
for i in illegal:
    if i == ")":
        score += 3
    elif i == "]":
        score += 57
    elif i == "}":
        score += 1197
    elif i == ">":
        score += 25137
print(score)

# Part Two
scores = []
for i in range(len(f)):
    a = []
    illegal = False
    for j in range(len(f[i])):
        closings = [")", ">", "]", "}"]
        if f[i][j] in openings:
            a.append(f[i][j])
        elif (f[i][j] == ")" and a[len(a)-1] == "(") or (f[i][j] == "]" and a[len(a)-1] == "[") or (f[i][j] == ">" and a[len(a)-1] == "<") or (f[i][j] == "}" and a[len(a)-1] == "{"):
            a.pop(len(a)-1)
        else:
            illegal = True
            break
    if illegal == False:
        cur_score = 0
        for j in range(len(a)-1, -1, -1):
            cur_score *= 5
            if a[j] == "(":
                cur_score += 1
            elif a[j] == "[":
                cur_score += 2
            elif a[j] == "{":
                cur_score += 3
            elif a[j] == "<":
                cur_score += 4
        scores.append(cur_score)
print(median(scores))