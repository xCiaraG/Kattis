from operator import itemgetter
line = list(map(int, input().strip().split()))
cost = line[1]
listeners = list(map(int, input().strip().split()))
profit = [x - cost for x in listeners]
profit[0] = (profit[0], profit[0])
i = 1
while i < len(profit):
	profit[i] = (profit[i], max(profit[i], profit[i]+profit[i-1][1]))
	i += 1
print(max(profit, key=itemgetter(1))[1])
