import math
line = list(map(int, input().strip().split()))
m = 0
prices = []
p = line[0]
a = line[1]
b = line[2]
c = line[3]
d = line[4]
for i in range(1, line[-1]+1):
    price = p*(math.sin((a*i)+b)+math.cos((c*i)+d)+2)
    prices.append(price)
if len(prices) > 1:
    m = prices[0] - prices[1]
j = 0
m = 0
md = 0
while j < len(prices):
	if prices[j] > m:
		m = prices[j]
	if m - prices[j] > md:
		md = m - prices[j]
	j += 1

if md > 0: 
    print(md)
else:
    print(0.00)