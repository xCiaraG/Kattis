from sys import stdin

def bfs(b, x, y, n, m, ansx, ansy):
	to_check = [(x+1, y, 1), (x-1, y, 1), (x, y-1, 1), (x, y+1, 1)]
	seen = set((x, y))
	while to_check:
		x, y, count = to_check.pop(0)
		if 0 <= x < n and 0 <= y < m and (x, y) not in seen and b[x][y] not in "*DX":
			seen.add((x, y))
			if x == ansx and y == ansy:
				return count
			to_check += [(x+1, y, count + 1), (x, y+1, count + 1), (x-1, y, count + 1), (x, y-1, count + 1)]
	return 0

n, m = [int(x) for x in stdin.readline().split()]
board = [list(stdin.readline().strip()) for _ in range(n)]
targets = []
for i in range(n):
	for j in range(m):
		if board[i][j] == "D":
			if i > 0:
				targets.append((i-1, j))
			if j > 0:
				targets.append((i, j-1))
			if i < n - 1:
				targets.append((i+1, j))
			if j < m - 1:
				targets.append((i, j+1))

ans = "KAKTUS"
for x, y in targets:
	water_distance = n*m
	fox_distance = n*m			
	for i in range(n):
		for j in range(m):
			if board[i][j] == "S":
				tmp = bfs(board, i, j, n, m, x, y)
				if tmp:
					fox_distance = tmp
			elif board[i][j] == "*":
				tmp = bfs(board, i, j, n, m, x, y)
				if tmp and tmp < water_distance:
					water_distance = tmp
	if board[x][y] == "*":
		water_distance = 0
	elif board[x][y] == "S":
		fox_distance = 0
	if water_distance > fox_distance and fox_distance < ans:
		ans = fox_distance + 1

print(ans)
