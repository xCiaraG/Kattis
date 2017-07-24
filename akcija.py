import sys
n = int(sys.stdin.readline().strip())
prices = []
for i in range(0, n):
    p = int(sys.stdin.readline().strip())
    prices.append(p)
prices.sort()
prices.reverse()
i = 0
total = 0
while i < len(prices):
    if not (i+1) % 3 == 0:
        total +=prices[i]
    i += 1
print(total)
