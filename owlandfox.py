import sys
n = int(sys.stdin.readline().strip())
for i in range(0,n):
    tmp = sys.stdin.readline().strip()
    line = []
    for c in tmp:
        line.append(c)
    i = len(line) - 1
    a = True
    while i != -1 and a:
        if line[i] != "0":
            m = int(line[i]) - 1
            line[i] = str(m)
            a = False
        i -= 1
    print(int("".join(line)))
