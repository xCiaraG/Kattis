import sys
lines = sys.stdin.readlines()
i = 0
count = 1
while i < len(lines) - 2:
    row1 = list(map(int, lines[i].strip().split()))
    row2 = list(map(int, lines[i+1].strip().split()))
    determinant = row1[0]*row2[1] - row1[1]*row2[0]
    tmp = row1[0]
    row1[0] = row2[1]//determinant
    row2[1] = tmp//determinant
    row1[1] = -row1[1]//determinant
    row2[0] = -row2[0]//determinant
    print("Case {}:".format(count))
    print("{} {}".format(row1[0], row1[1]))
    print("{} {}".format(row2[0], row2[1]))
    count += 1
    i += 3
