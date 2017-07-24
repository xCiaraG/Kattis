import sys
n = int(sys.stdin.readline().strip())
l = []
for i in range(0, n):
    line = sys.stdin.readline().strip().split()
    if line[0][0] in "0123456789":
        l.append((int(line[0]), line[1]))
    else:
        l.append((int(line[1])*2, line[0]))

l.sort()
for t in l:
    print(t[1])
