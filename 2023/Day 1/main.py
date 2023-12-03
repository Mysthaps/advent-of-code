with open("input.txt") as f:
    f = f.readlines()

part_1_answer = 0
part_2_answer = 0

def get_number(line, idx, text):
    if line[idx].isnumeric():
        return int(line[idx])
    
    if text:
        if line[idx:idx+3] == "one": return 1
        elif line[idx:idx+3] == "two": return 2
        elif line[idx:idx+5] == "three": return 3
        elif line[idx:idx+4] == "four": return 4
        elif line[idx:idx+4] == "five": return 5
        elif line[idx:idx+3] == "six": return 6
        elif line[idx:idx+5] == "seven": return 7
        elif line[idx:idx+5] == "eight": return 8
        elif line[idx:idx+4] == "nine": return 9
        elif line[idx:idx+4] == "zero": return 0

    return False


for line in f:
    nump1 = ["a", "a"]
    nump2 = ["a", "a"]
    for i in range(len(line)):
        if get_number(line, i, False) != False:
            if nump1[0] == "a": nump1[0] = get_number(line, i, False)
            nump1[1] = get_number(line, i, False)

        if get_number(line, i, True) != False:
            if nump2[0] == "a": nump2[0] = get_number(line, i, True)
            nump2[1] = get_number(line, i, True)

    try:
        part_1_answer = part_1_answer + nump1[0] * 10 + nump1[1]
        part_2_answer = part_2_answer + nump2[0] * 10 + nump2[1]
    except:
        continue

print("Part 1:", part_1_answer)
print("Part 2:", part_2_answer)
