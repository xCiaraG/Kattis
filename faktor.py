n = list(map(int, input().strip().split()))
tmp = n[0] * n[1] 
while tmp / n[0] > n[1] - 1:
    tmp -= 1
print(tmp + 1)
