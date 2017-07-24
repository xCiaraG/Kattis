import sys
line = list(map(int, sys.stdin.readline().strip().split()))
t = line[0] + line[1]
price = line[2]
total = 0
while t >= price:
    total += t//price
    t = t//price + t % price
print(total)
