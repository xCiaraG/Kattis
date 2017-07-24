import sys
n = int(sys.stdin.readline().strip())
for i in range(0,n):
    calories = int(sys.stdin.readline().strip())
    if calories % 400 != 0:
        print(calories//400 + 1)
    else:
        print(calories//400)
