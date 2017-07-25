n = int(input())
while n != -1:
	graph = []
	for i in range(0, n):
		line = [(i, x+i) for x, y in enumerate(input().split()[i:]) if int(y)]
		graph += line
	ans = [False]*n
	for i in range(0, n):
		to_check = []
		for v in graph:
			if v[0] == i:
				to_check.append(v[1])
			elif v[1] == i:
				to_check.append(v[0])
		for p in to_check:
			for v in graph:
				if v[0] == p and v[1] != i and ((v[1], i) in graph or (i, v[1]) in graph):
					ans[i] = True
				elif v[1] == p and v[0] != i and ((v[0], i) in graph or (i, v[0]) in graph):
					ans[i] = True
	print(*[x for x, y in enumerate(ans) if not y])
	n = int(input())
