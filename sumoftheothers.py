import sys
lines = sys.stdin.readlines()
for line in lines:
    line = list(map(int, line.strip().split()))
    print(sum(line)//2)
