import sys
n = int(sys.stdin.readline().strip())
for k in range(0,n):
    line = list(map(int, sys.stdin.readline().strip().split()))
    number = int(line[1])
    total, total_even, total_odd = 0, 0, 0
    total = number*(number+1)//2
    total_even = number*(number+1)
    total_odd = number*(number)
    print(k+1, total, total_odd, total_even)
