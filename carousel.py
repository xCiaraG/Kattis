line = list(map(int, input().strip().split()))
while line != [0, 0]:
	m = line[1]
	n = line[0]
	buy = []
	for i in range(0, n):
		tickets = list(map(int, input().strip().split()))
		if tickets[0] <= m:
			if not buy:
				buy = [(tickets[0], tickets[1])]
			elif tickets[1]/tickets[0] < buy[0][1]/buy[0][0]:
				buy = [(tickets[0], tickets[1])]
			elif tickets[1]/tickets[0] == buy[0][1]/buy[0][0]:
				buy.append((tickets[0], tickets[1]))
	if buy:
		buy = sorted(buy)
		print("Buy {} tickets for ${}".format(buy[-1][0], buy[-1][1]))
	else:
		print("No suitable tickets offered")
	line = list(map(int, input().strip().split()))
