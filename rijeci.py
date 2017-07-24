import sys
n = int(sys.stdin.readline().strip())
count = [0,1]
for i in range(0, n-1):
    tmp = count[0]
    count[0] = count[1]
    count[1] += tmp

print(count[0], count[1])
