with open("input.txt") as f:
    f = list(map(str, f.read().split("\n\n")))
    #f = [i.split() for i in f]

# Part One
n = 0

for i in f:
    if "byr" in i and "iyr" in i and "eyr" in i and "hgt" in i and "hcl" in i and "ecl" in i and "pid" in i:
        n += 1
    else:
        f.remove(i)

print(n)

# Part Two :edegabudgetcuts:
n = 0
f = [i.split() for i in f]
f = [[j.split(":") for j in i] for i in f]

for i in f:
    valid = True
    i.sort()
    for j in i:
        if j[0] == 'byr':
            if int(j[1]) >= 1920 and int(j[1]) <= 2002:
                pass
            else:
                break
        if j[0] == 'iyr':
            if int(j[1]) >= 2010 and int(j[1]) <= 2020:
                pass
            else:
                break
        if j[0] == 'eyr':
            if int(j[1]) >= 2020 and int(j[1]) <= 2030:
                pass
            else:
                break
        if j[0] == 'hgt':
            if 'cm' in j[1]:
                j[1] = j[1].strip('cm')
                if int(j[1]) >= 150 and int(j[1]) <= 193:
                    pass
                else:
                    break
            elif 'in' in j[1]:
                j[1] = j[1].strip('in')
                if int(j[1]) >= 59 and int(j[1]) <= 76:
                    pass
                else:
                    break
            else:
                break
        if j[0] == 'hcl':
            if len(j[1]) != 7:
                break
            elif j[1][0] != "#":
                break
            else:
                for k in j[1]:
                    if k in "#0123456789abcdef":
                        pass
                    else:
                        break
        if j[0] == 'ecl':
            if j[1] == "amb" or j[1] == "blu" or j[1] == "brn" or j[1] == "gry" or j[1] == "grn" or j[1] == "hzl" or j[1] == "oth":
                pass
            else:
                break
        if j[0] == 'pid':
            if len(j[1]) == 9:
                pass
            else:
                break
    else:
        print(i)
        n += 1
print(n)