import sys
n = int(sys.stdin.readline().strip())
for i in range(0,n):
    tmp = int(sys.stdin.readline().strip())
    if tmp % 2 == 0:
        print(tmp, "is even")
    else:
        print(tmp, "is odd")
