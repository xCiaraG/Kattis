def valid(x, y):
	return 0 <= x <= 7 and 0 <= y <= 7 and board[x][y] in ".D"

def ice(x, y):
	return 0 <= x <= 7 and 0 <= y <= 7 and board[x][y] == "I"

def execute(direction, instructions):
	x, y = 7, 0
	while instructions:
		current = instructions[0]
		instructions = instructions[1:]
		if current == "R":
			direction = (direction + 1) % 4
		elif current == "L":
			direction = (direction - 1) % 4
		elif current == "F":
			if direction == 1 and valid(x, y + 1):
				y += 1
			elif direction == 2 and valid(x + 1, y):
				x += 1
			elif direction == 3 and valid(x, y - 1):
				y -= 1
			elif direction == 0 and valid(x - 1, y):
				x -= 1
			else:
				return "Bug!"
		else:
			if direction == 1 and ice(x, y + 1):
				board[x][y + 1] = "."
			elif direction == 2 and ice(x + 1, y):
				board[x + 1][y] = "."
			elif direction == 3 and ice(x, y - 1):
				board[x][y - 1]
			elif direction == 0 and ice(x - 1, y):
				board[x - 1][y] = "."
			else:
				return "Bug!"

	if valid(x, y) and board[x][y] == "D":
		return "Diamond!"
	else:
		return "Bug!"

board = []
for i in range(8):
	board.append(list(input().strip()))
board[7][0] = "."
instructions = input().strip()
direction = 1
print(execute(direction, instructions))