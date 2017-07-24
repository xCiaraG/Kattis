import sys
line = list(map(int, sys.stdin.readline().strip().split()))
total = line[1]
line = list(map(int, sys.stdin.readline().strip().split()))
count = 0
for n in line:
    total -= n
    if total >=0:
        count += 1
print(count)
