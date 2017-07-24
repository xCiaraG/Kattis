line = list(map(int, input().strip().split()))
while line != [0]:
	front = list(map(int, input().strip().split()))
	rear = list(map(int, input().strip().split()))
	ratio = []
	i = 0
	while i < len(front):
		j = 0
		while j < len(rear):
			ratio.append(rear[j]/front[i])
			j += 1
		i += 1
	ratio = sorted(ratio)
	spread = []
	i = 0
	while i + 1 < len(ratio):
		spread.append(ratio[i+1]/ratio[i])
		i += 1
	print("{:.2f}".format(max(spread)))

	line = list(map(int, input().strip().split()))