import sys
line = sys.stdin.readline().strip()
d = {}
for c in line:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1

count = 0
for key in d:
    if d[key] % 2 != 0:
        count += 1
if count != 0:
    print(count - 1)
else:
    print(0)
