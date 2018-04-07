from sys import stdin
n = int(stdin.readline())
for i in range(n):
	m, minimum = [int(x) for x in stdin.readline().strip().split()]
	numbers = [int(x) for x in stdin.readline().strip().split()]
	max_sum = 0
	current = []
	contains_min = False
	for n in numbers:
		if n < minimum:
			if contains_min:
				max_sum = max(max_sum, sum(current))
			current = []
			contains_min = False
		elif n == minimum and not contains_min:
			current.append(n)
			contains_min = True
		elif n == minimum:
			max_sum = max(max_sum, sum(current))
			current = current[current.index(n) + 1:] + [n]
		else:
			current.append(n)
	if contains_min:
		 max_sum = max(max_sum, sum(current))
	print(max_sum)

	