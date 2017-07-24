import sys
n = int(sys.stdin.readline().strip())
s = 0
for i in range(0, n):
    n = sys.stdin.readline().strip()
    s += int(n[:len(n)-1])**int(n[-1])

print(s)

