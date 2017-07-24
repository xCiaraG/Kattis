import sys
prices = list(map(int, sys.stdin.readline().strip().split()))
truck1 = list(map(int, sys.stdin.readline().strip().split()))
truck2 = list(map(int, sys.stdin.readline().strip().split()))
truck3 = list(map(int, sys.stdin.readline().strip().split()))
d = {}
for i in range(truck1[0], truck1[1]):
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1 
for i in range(truck2[0], truck2[1]):
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1 
for i in range(truck3[0], truck3[1]):
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1 
total = 0
for key in d:
    if d[key] == 1:
        total += prices[0]
    elif d[key] == 2:
        total += prices[1]*2
    else: 
        total += prices[2]*3
print(total)
