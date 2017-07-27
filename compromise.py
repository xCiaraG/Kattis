n = int(input())
for i in range(0, n):
	line = [int(x) for x in input().split()]
	result = [0]*line[1]
	for j in range(0, line[0]):
		s = input().strip()
		k = 0
		while k < len(s):
			result[k] += int(s[k])
			k += 1
		j += 1
	j = 0
	while j < len(result):
		if result[j] >= line[0]/2:
			result[j] = 1
		else:
			result[j] = 0
		j += 1
	print("".join(list(map(str, result))))