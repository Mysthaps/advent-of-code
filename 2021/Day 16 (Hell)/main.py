with open("input.txt") as f:
    f = f.read()
    length = len(f) * 4
    f = (bin(int(f, 16))[2:]).zfill(length)

# Part One

