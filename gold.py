def go(pi, pj):
	global count
	to_do = [(pi+1, pj), (pi-1, pj), (pi, pj+1), (pi, pj-1)]
	while to_do:
		pi, pj = to_do[0]
		to_do = to_do[1:]
		if board[pi][pj] == "G":
			count += 1
		if board[pi][pj] != "#" and board[pi+1][pj] != "T" and board[pi-1][pj] != "T" and board[pi][pj+1] != "T" and board[pi][pj-1] != "T":
			to_do.append((pi, pj-1))
			to_do.append((pi, pj+1))
			to_do.append((pi-1, pj))
			to_do.append((pi+1, pj))
		board[pi][pj] = "#"
	
x, y = [int(x) for x in input().split()]
board = []

for i in range(0, y):
	board.append(list(input().strip()))

for i in range(0, y):
	for j in range(0, x):
		if board[i][j] == "P":
			pi, pj = i, j
count = 0			
if board[pi+1][pj] != "T" and board[pi-1][pj] != "T" and board[pi][pj+1] != "T" and board[pi][pj-1] != "T":
	go(pi, pj)
print(count)