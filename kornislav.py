import sys
m = list(map(int,sys.stdin.readline().strip().split()))
m = sorted(m)
print(m[0]*m[2])
