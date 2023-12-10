with open("input.txt") as f:
    f = f.read().split("\n")
    f = [[int(j) for j in i.split()] for i in f]

board = [[0 for _ in range(25)] for _ in range(25)]
part_1_answer = 0
part_2_answer = 0

for line in f:
    for i in range(len(line)):
        for j in range(i, len(line)):
            if i == 0: board[i][j] = line[j]
            else: board[i][j] = board[i-1][j] - board[i-1][j-1]
            if j == len(line) - 1:
                part_1_answer = part_1_answer + board[i][j]

for line in f:
    cur = 0
    for i in range(len(line)):
        for j in range(len(line)-i):
            if i == 0: board[i][j] = line[j]
            else: board[i][j] = board[i-1][j+1] - board[i-1][j]
        if i == len(line) - 1:
            for j in range(i, -1, -1):
                cur = board[j][0] - cur
            part_2_answer = part_2_answer + cur

print("Part 1:", part_1_answer)
print("Part 2:", part_2_answer)