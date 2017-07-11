import sys
lines = sys.stdin.readlines()
for line in lines:
    line = line.strip().split("/")
    count = 1
    n = int(line[1])**2
    p = 2
    t = 1
    c = 1
    while n % p == 0:
        n = n//p
        c += 1
    p += 1
    t *= c
    p = 3
    while n != 1:
        c = 1
        while n % p == 0:
            n = n//p
            c += 1
        p += 2
        t *= c
    if t % 2 == 0:
        print(t//2)
    else:
        print((t+1)//2)