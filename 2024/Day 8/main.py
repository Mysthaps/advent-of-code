with open("input.txt") as f:
    f = f.read().split("\n")
    f = [[j for j in i] for i in f]

antinodes_p1 = []
antinodes_p2 = []
part_1 = 0
part_2 = 0
for i in range(len(f)):
    antinodes_p1.append([])
    antinodes_p2.append([])
    for j in range(len(f[i])):
        antinodes_p1[i].append('.')
        antinodes_p2[i].append('.')
        
for i in range(len(f)):
    for j in range(len(f[i])):
        for x in range(len(f)):
            for y in range(len(f[x])):
                if f[i][j] == f[x][y] and f[i][j] != '.':
                    offx, offy = x-i, y-j
                    ### Part 1 ###
                    if not (i == x and j == y) and x + offx < len(f) and x + offx >= 0 and y + offy < len(f[x]) and y + offy >= 0: 
                        if antinodes_p1[x+offx][y+offy] == '.':
                            antinodes_p1[x+offx][y+offy] = '#'
                            part_1 += 1

                    ### Part 2 ###
                    tempx, tempy = x, y
                    while tempx + offx < len(f) and tempx + offx >= 0 and tempy + offy < len(f[tempx]) and tempy + offy >= 0: 
                        if antinodes_p2[tempx+offx][tempy+offy] == '.':
                            antinodes_p2[tempx+offx][tempy+offy] = '#'
                            part_2 += 1
                        if offx == 0 and offy == 0: break
                        tempx += offx
                        tempy += offy

print("Part 1:", part_1)
print("Part 2:", part_2)