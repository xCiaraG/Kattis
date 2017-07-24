import sys
n = int(sys.stdin.readline().strip())
for i in range(0, n):
    line = list(map(int, sys.stdin.readline().strip().split()))
    prev = line[0]
    j = 1
    t = 0
    while j < len(line)-1:
        if line[j] - 2*prev > 0:
            t += line[j] - 2*prev
        prev = line[j]
        j += 1
    print(t)
