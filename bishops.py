import sys
lines = sys.stdin.readlines()
for line in lines:
    n = int(line.strip())
    if n > 2:
        print(n*2 - 2)
    else:
        print(n)