import sys
lines = sys.stdin.readlines()
for line in lines:
    line = line.strip().split()
    total = 0
    count = 0
    name = ""
    i = 0
    while line[i][0] in "0123456789":
        count += 1
        total += float(line[i])
        i += 1
    while i < len(line) and line[i][0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        name += line[i] + " "
        i += 1
    while i < len(line) and line[i][0] in "0123456789":
        count += 1
        total += float(line[i])
        i += 1
    print("{:.6f}".format(total/count), name)
