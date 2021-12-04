with open("input.txt") as f:
    f = f.read().split("\n\n")

seq = f[0].split(",")

def bingo(board):
    a = []
    for i in range(len(board)):
        a.append(board[i])
    for i in range(len(seq)):
        for j in range(len(board)):
            if board[j] == seq[i]:
                a[j] = "x"
            # Horizontal
            for k in range(0, len(a), 5):
                if a[k] == a[k+1] == a[k+2] == a[k+3] == a[k+4] == "x":
                    total = 0
                    for l in range(len(a)):
                        if a[l] != "x":
                            total += int(a[l])
                    return [total, int(seq[i]) ,i]
            # Vertical
            for k in range(0, 5):
                if a[k] == a[k+5] == a[k+10] == a[k+15] == a[k+20] == "x":
                    total = 0
                    for l in range(len(a)):
                        if a[l] != "x":
                            total += int(a[l])
                    return [total, int(seq[i]) ,i]

# Part One

x = 1
lowest = [0, 0, 999]
while True:
    try:
        board = f[x].split()
        stats = bingo(board)
        if stats[2] < lowest[2]:
            lowest = stats

        x += 1
    except:
        break

print(lowest[0] * lowest[1])

# Part Two

x = 1
highest = [0, 0, 0]
while True:
    try:
        board = f[x].split()
        stats = bingo(board)
        if stats[2] > highest[2]:
            highest = stats

        x += 1
    except:
        break

print(highest[0] * highest[1])