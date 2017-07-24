import sys
n = int(sys.stdin.readline().strip())
while n != -1:
    i = 0
    total = 0
    prev = 0
    while i < n:
        line = list(map(int,sys.stdin.readline().strip().split()))
        total += line[0]*(line[1]-prev)
        prev = line[1]
        i += 1
    print(total, "miles")
    n = int(sys.stdin.readline().strip())
