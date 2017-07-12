line = input().strip().split()
s = "1"
i = 0
if len(line) > 1:
    for letter in line[1]:
        if letter == "R":
            s += "1"
        else:
            s += "0"
print(((2**(int(line[0])+1))-(int(s, 2))))