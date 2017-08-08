n = int(input())
for i in range(0, n):
    m = int(input())
    d = {}
    for j in range(0, m):
        line = input().strip().split()
        if line[1] in d:
            d[line[1]] += 1
        else:
            d[line[1]] = 2
    t = 1
    for disguise in d:
        t *= d[disguise]
    print(t-1)