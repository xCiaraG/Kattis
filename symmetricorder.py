import sys
n = int(sys.stdin.readline().strip())
count = 1
while n != 0:
    l = [0]*n
    s = 0
    for i in range(0, n):
        name = sys.stdin.readline().strip()
        if i % 2 == 1:
            l[len(l)-1-s] = name
            s += 1
        else:
            l[s] = name
    print("SET", count)
    count += 1
    for name in l:
        print(name)
    n = int(sys.stdin.readline().strip())
