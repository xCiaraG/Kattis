line = input().strip().split()
while line != ["0.0", "0"]:
	fight_distance = float(line[0])
	n = int(line[1])
	to_check = []
	for i in range(0, n):
		line = list(map(float, input().strip().split()))
		to_check.append((line[0], line[1]))
	a = [0]*len(to_check)
	i = 0
	while i < len(to_check):
		j = i + 1
		while j < len(to_check):
			if ((to_check[i][0]-to_check[j][0])**2+ (to_check[i][1]-to_check[j][1])**2)**0.5 <= fight_distance:
				a[i] = 1
				a[j] = 1
			j += 1
		i += 1
	print("{} sour, {} sweet".format(sum(a), len(a)-sum(a)))
	line = input().strip().split()
