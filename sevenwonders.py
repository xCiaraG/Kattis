import sys
n = sys.stdin.readline().strip()
d = {}
for c in n:
    if c not in d:
        d[c] = 1
        minimum = c
    else: 
        d[c] += 1

t = 0
minimum = d[minimum] 
count = 0
for key in d:
    t += d[key]**2
    if d[key] < minimum:
        minimum = d[key]
if len(d) == 3:
    t += 7*minimum
print(t)
