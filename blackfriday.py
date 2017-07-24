import sys
n = int(sys.stdin.readline().strip())
rolls = list(map(int, sys.stdin.readline().strip().split()))
d = {}
for n in rolls:
    if n not in d:
        d[n] = 1
    else:
        d[n] += 1
m = 0
for key in d:
    if key > m and d[key] == 1:
        m = key
if m != 0:
    print(rolls.index(m)+1)
else:
    print("none")
