win_combinations = ["r1", "r2", "r3", "c1", "c2", "c3", "d1", "d2",\
					"r1c1", "r1c2", "r1c3", "r1d1", "r1d2" "r2c1",\
					"r2c2", "r2c3", "r2d1", "r2d2" "r3c1", "r3c2", "r3c3",\
					"r3d1", "r3d2", "c1d1", "c1d2", "c2d1", "c2d2",\
					"c3d1", "c3d2", "d1d2"]
def count(board, p):
	total = 0
	for r in board:
		for c in r:
			if c == p:
				total += 1
	return total

def wins(board, p):
	win = ""
	if len(set(board[0])) == 1 and board[0][0] == p:
		win += "r1"
	if len(set(board[1])) == 1 and board[1][0] == p:
		win += "r2"
	if len(set(board[2])) == 1 and board[2][0] == p:
		win += "r3"
	if board[0][0] == board[1][0] == board[2][0] == p:
		win += "c1"
	if board[0][1] == board[1][1] == board[2][1] == p:
		win += "c2"
	if board[0][2] == board[1][2] == board[2][2] == p:
		win += "c3"
	if board[0][0] == board[1][1] == board[2][2] == p:
		win += "d1"
	if board[0][2] == board[1][1] == board[2][0] == p:
		win += "d2"
	return win

def configuration(board):
	if count(board, "O") != count(board, "X") and count(board, "X") != count(board, "O") + 1:
		return False
	elif count(board, "O") == count(board, "X") and wins(board, "X"):
		return False
	elif count(board, "O") + 1 == count(board, "X") and wins(board, "O"):
		return False
	elif wins(board, "X") and wins(board, "O"):
		return False
	elif (wins(board, "X") and wins(board, "X") not in win_combinations) or (wins(board, "O") and wins(board, "O") not in win_combinations):
		return False
	return True


n = int(input())
for i in range(n-1):
	board = [[x for x in input().strip()] for i in range(3)]
	if configuration(board):
		print("yes")
	else:
		print("no")
	input()

board = [[x for x in input().strip()] for i in range(3)]
if configuration(board):
	print("yes")
else:
	print("no")