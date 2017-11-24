n, m = [int(x) for x in input().split()]
dishes = [list(input().strip()) for i in range(n)]
visited = set()
loops = 0
for i in range(n):
	for j in range(m):
		if (i, j) not in visited and dishes[i][j] == "#":
			loops += 1
		to_check = [(i, j)]
		while to_check:
			current = to_check.pop(0)
			a, b = current[0], current[1]
			if 0 <= a < n and 0 <= b < m and current not in visited:
				visited.add(current)
				if dishes[a][b] == "#":
					to_check += [(a + 1, b), (a - 1, b), (a, b - 1), (a, b + 1), (a - 1, b - 1), (a + 1, b + 1), (a - 1, b + 1), (a + 1, b - 1)]
print(loops)
