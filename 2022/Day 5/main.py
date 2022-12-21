with open("input.txt") as f:
    f = f.read().split("\n")
    f = [i.split(" ") for i in f]

boxes = [
        ["Q", "F", "L", "S", "R"],
        ["T", "P", "G", "Q", "Z", "N"],
        ["B", "Q", "M", "S"],
        ["Q", "B", "C", "H", "J", "Z", "G", "T"],
        ["S", "F", "N", "B", "M", "H", "P"],
        ["G", "V", "L", "S", "N", "Q", "C", "P"],
        ["F", "C", "W"],
        ["M", "P", "V", "W", "Z", "G", "H", "Q"],
        ["R", "N", "C", "L", "D", "Z", "G"]
        ]
boxes2 = [
        ["Q", "F", "L", "S", "R"],
        ["T", "P", "G", "Q", "Z", "N"],
        ["B", "Q", "M", "S"],
        ["Q", "B", "C", "H", "J", "Z", "G", "T"],
        ["S", "F", "N", "B", "M", "H", "P"],
        ["G", "V", "L", "S", "N", "Q", "C", "P"],
        ["F", "C", "W"],
        ["M", "P", "V", "W", "Z", "G", "H", "Q"],
        ["R", "N", "C", "L", "D", "Z", "G"]
        ]

for i in range(len(f)):
    amt = int(f[i][1])
    frm = int(f[i][3])-1
    to = int(f[i][5])-1
    while amt > 0 and len(boxes[frm]) > 0 and len(boxes2[frm]) > 0:
        boxes[to].insert(0, boxes[frm].pop(0))
        boxes2[to].insert(int(f[i][1]) - amt, boxes2[frm].pop(0))
        amt -= 1


for i in boxes:
    print(i[0], end = "")
print()
for i in boxes2:
    print(i[0], end = "")