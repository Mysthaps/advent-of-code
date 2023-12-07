with open("input.txt") as f:
    f = f.readlines()

part_1_answer = 0
part_2_answer = 0

cards = []
copies = []

for line in f:
    card = [[], []]
    check = False
    for item in line.split():
        if item == "|": check = True
        if item.isnumeric():
            if check == False: card[0].append(int(item))
            else: card[1].append(int(item))
    cards.append(card)
    copies.append(1)

for i in range(len(cards)):
    card = cards[i]
    score = 0
    for num in card[1]:
        if num in card[0]: score = score + 1
    for j in range(i, i + score):
        copies[j+1] = copies[j+1] + copies[i]

    if score > 0: part_1_answer = part_1_answer + pow(2, score-1)
part_2_answer = sum(copies)

print("Part 1:", part_1_answer)
print("Part 2:", part_2_answer)
