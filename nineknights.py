def all_valid(board):
	for i in range(5):
		for j in range(5):
			if board[i][j] == "k":
				if i > 0 and j > 1 and board[i-1][j-2] == "k":
					return False
				elif i > 1 and j > 0 and board[i-2][j-1] == "k":
					return False
				elif i < 4 and j < 3 and board[i+1][j+2] == "k":
					return False
				elif i < 3 and j < 4 and board[i+2][j+1] == "k":
					return False
				elif i > 0 and j < 3 and board[i-1][j+2] == "k":
					return False
				elif i > 1 and j < 4 and board[i-2][j+1] == "k":
					return False
				elif i < 4 and j > 1 and board[i+1][j-2] == "k":
					return False
				elif i < 3 and j > 0 and board[i+2][j-1] == "k":
					return False
	return True  

board = [[l for l in input().strip()] for i in range(5)]

if sum([l.count("k") for l in board]) == 9:
	if all_valid(board):
		print("valid")
	else:
		print("invalid")
else:
	print("invalid")