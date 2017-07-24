import sys
numbers = list(map(int, sys.stdin.readline().strip().split()))
for i in range(0,numbers[0]):
    line = sys.stdin.readline().strip()
    new_s = ""
    for c in line:
        new_s += numbers[3]*c
    for i in range(0, numbers[2]):
        print(new_s)
