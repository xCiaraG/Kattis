import sys
n = int(sys.stdin.readline().strip())
for i in range(0,n):
    line = list(map(int,sys.stdin.readline().strip().split()))
    d = 2**line[0]
    if (line[1] - (d-2)) -1 == 0 or (line[1]-(d-2)-1) % d == 0:
        print("Case #{}: ON".format(i+1))
    else:
        print("Case #{}: OFF".format(i+1))
