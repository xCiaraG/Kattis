import sys
cost = float(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())
total = 0
for i in range(0,n):
    tmp = list(map(float, sys.stdin.readline().strip().split()))
    total += tmp[0]*tmp[1]*cost
print("{:.7f}".format(total))
