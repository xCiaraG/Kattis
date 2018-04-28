n = int(input())
for _ in range(n):
    m = int(input())
    a = 1
    b = 1
    for _ in range(m):
        tmp = a
        a += b
        b = tmp
        a %= (10**9 + 7)
        b %= (10**9 + 7)
    print(a)