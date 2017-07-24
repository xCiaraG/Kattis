import sys, math
line = list(map(int, sys.stdin.readline().strip().split()))
print(int((line[0]//math.sin(math.radians(line[1]))) + 1))
