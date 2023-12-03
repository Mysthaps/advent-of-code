with open("input.txt") as f:
    f = f.readlines()

part_1_answer = 0
part_2_answer = 0

for line in f:
    result = {"red": 0, "green": 0, "blue": 0}
    state = line.split()
    for i in range(len(state)):
        if state[i].isnumeric():
            if state[i+1][-1] == "," or state[i+1][-1] == ";":
                result[state[i+1][:-1]] = max(result[state[i+1][:-1]], int(state[i]))
            else:
                result[state[i+1]] = max(result[state[i+1]], int(state[i]))
    if result["red"] <= 12 and result["green"] <= 13 and result["blue"] <= 14:
        part_1_answer = part_1_answer + int(state[1][:-1])
    part_2_answer = part_2_answer + result["red"] * result["green"] * result["blue"]

print("Part 1:", part_1_answer)
print("Part 2:", part_2_answer)
