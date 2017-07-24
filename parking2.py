import sys
n = int(sys.stdin.readline().strip())
for i in range(0, n):
    m = int(sys.stdin.readline().strip())
    l = list(map(int, sys.stdin.readline().strip().split()))
    l.sort()
    print((l[len(l)-1]-l[0])*2)
