from sys import stdin
import heapq
def bfs(board, x1, y1):
	to_visit = [(0,x1,y1)]
	while to_visit:
		c, x2, y2 = heapq.heappop(to_visit)
		if board[x2][y2] != "#":
			if board[x2][y2] == "D" and (x2 == 0 or y2 == 0 or x2 == n-1 or y2 == m-1):
				return c
			if board[x2][y2] == "c":
				c += 1
			board[x2][y2] = "#"
			if x2 > 0 and board[x2-1][y2] != "#":
				heapq.heappush(to_visit, (c,x2-1,y2))
			if x2 < n-1 and board[x2+1][y2] != "#":
				heapq.heappush(to_visit, (c,x2+1,y2))
			if y2 > 0 and board[x2][y2+1] != "#":
				heapq.heappush(to_visit, (c,x2,y2+1))
			if y2 < m-1 and board[x2][y2-1] != "#":
				heapq.heappush(to_visit, (c,x2,y2-1))

n, m = [int(x) for x in stdin.readline().split()]
board = [0]*n
for i in range(n):
	board[i] = list(stdin.readline().strip())

x, y = [int(x) for x in stdin.readline().split()]
print(bfs(board, x-1, y-1))