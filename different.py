import sys
lines = sys.stdin.readlines()
for line in lines:
    line = list(map(int, line.strip().split()))
    print(abs(line[1]-line[0]))
