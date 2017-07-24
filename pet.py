import sys
m = (0,0)
for i in range(0,5):
    tmp = list(map(int, sys.stdin.readline().strip().split()))
    count = 0
    for n in tmp:
        count += n
    if count > m[1]:
        m = (i+1, count)
print(m[0], m[1])
