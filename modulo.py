import sys
c = 0
l = []
for i in range(0, 10):
    n = int(sys.stdin.readline().strip())
    if n % 42 not in l:
        l.append(n%42)
        c += 1
print(c)
