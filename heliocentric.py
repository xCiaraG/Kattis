import sys
lines = sys.stdin.readlines()
i = 1
for line in lines:
    line = list(map(int, line.strip().split()))
    if line[0] != 0:
        mars = (line[1] + 365 - line[0]) % 687
        total = 365 - line[0]
    else:
        mars = line[1]
        total = 0
    while mars != 0:
        mars = (mars + 365) % 687
        total += 365
    print("Case {}: {}".format(i, total))
    i += 1
