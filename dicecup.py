import sys
line = list(map(int, sys.stdin.readline().strip().split()))
i = line[0]
j = line[1]
d = {}
for i in range(1, i+1):
    for j in range(1, j+1):
        if i+j not in d:
            d[i+j] = 1
        else:
            d[i+j] += 1
m = 0
k = []
for key in d:
    if d[key] > m:
        m = d[key]
        k = [key]
    elif d[key] == m:
        k.append(key)
k = list(map(str, sorted(k)))
for n in k:
    print(n)
