import sys
n = int(sys.stdin.readline().strip())
for i in range(0, n):
    m = list(map(int,sys.stdin.readline().strip().split()))
    m = m[0]
    lines = []
    for j in range(0,m):
        lines.append(sys.stdin.readline().strip())
    lines.reverse()
    print("Test", i+1)
    for line in lines:
        print(line[::-1])
