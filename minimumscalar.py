n = int(input().strip())
for i in range(0, n):
    m = input()
    v1 = list(map(int, input().strip().split()))
    v2 = list(map(int, input().strip().split()))
    v1 = sorted(v1)
    v2 = sorted(v2)
    v2.reverse()
    j = 0
    t = 0
    while j < len(v1):
        t += v1[j] * v2[j]
        j += 1
    print("Case #{}: {}".format(i+1, t))
