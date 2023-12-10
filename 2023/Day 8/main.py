import numpy as np

with open("input.txt") as f:
    f = f.read().split("\n")

instructions = ""
nodes = {}
current_nodes = []
nodes_results = []

part_1_answer = 0

for line in f:
    line = line.split(" = ")
    if len(line) == 1:
        if instructions == "": 
            instructions = line[0]
        continue
    nodes[line[0]] = line[1][1:-1].split(", ")
    if line[0][-1] == "A": 
        current_nodes.append(line[0])
        nodes_results.append(0)

current = "AAA"
inst = 0
while current != "ZZZ":
    if inst == len(instructions): inst = 0
    if instructions[inst] == "L": current = nodes[current][0]
    else: current = nodes[current][1]
    inst = inst + 1
    part_1_answer = part_1_answer + 1

for idx in range(len(current_nodes)):
    inst = 0
    while current_nodes[idx][-1] != "Z":
        if inst == len(instructions): inst = 0
        if instructions[inst] == "L": current_nodes[idx] = nodes[current_nodes[idx]][0]
        else: current_nodes[idx] = nodes[current_nodes[idx]][1]
        inst = inst + 1
        nodes_results[idx] = nodes_results[idx] + 1

print("Part 1:", part_1_answer)
print("Part 2:", np.lcm.reduce(nodes_results, dtype=np.int64))
