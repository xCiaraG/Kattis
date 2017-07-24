import sys
n = sys.stdin.readline().strip()
n = sys.stdin.readline().strip().split()
c = 0
for temp in n:
    if int(temp) < 0:
        c += 1
print(c) 
