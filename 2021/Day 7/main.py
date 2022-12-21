from statistics import median, mean

with open("input.txt") as f:
    f = f.read().split(",")
    f = [int(i) for i in f]
    
# Part One

fuel = 0
for i in range(len(f)):
    fuel += int(abs(f[i] - median(f)))

print(fuel)

# Part Two

fuel = 0
for i in range(len(f)):
    fuel += sum(range(1, abs(f[i] - sum(f)//len(f)) + 1))

print(fuel)