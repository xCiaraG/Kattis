from sys import stdin
from collections import deque

def bfs(x, y):
	to_check = deque([(x, y)])
	while to_check:
		x, y = to_check.popleft()
		if grid[x][y] == "C" or grid[x][y] == "L":
			grid[x][y] = "W"
			for x, y in [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]:
				if 0 <= x < n and 0 <= y < m:
					to_check.append((x, y))

n, m = [int(x) for x in stdin.readline().split()]
grid = [list(stdin.readline().strip()) for i in range(n)]
count = 0
for i in range(n):
	for j in range(m):
		if grid[i][j] == "L":
			bfs(i, j)
			count += 1
print(count)