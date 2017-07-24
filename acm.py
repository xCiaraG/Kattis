import sys
line = sys.stdin.readline().strip().split()
d = {}
while line != ["-1"]:
    if line[1] not in d:
        if line[2] == "wrong":
            d[line[1]] = [line[2], 20]
        else:
            d[line[1]] = [line[2], int(line[0])]
    elif line[2] == "wrong":
        d[line[1]][1] += 20
    else:
        d[line[1]][0] = "right"
        d[line[1]][1] += int(line[0])
    line = sys.stdin.readline().strip().split()
count = 0
total = 0
for key in d:
    if d[key][0] == "right":
        count   += 1
        total += d[key][1] 

print(count, total)
