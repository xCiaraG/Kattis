board = []
for i in range(0, 7):
    new = input()
    line = []
    for c in new:
        line.append(c)
    board.append(line)

count = 0
i = 0
while i < len(board):
    j = 0
    while j < len(board[i]):
        if board[i][j] == "o" and j > 1 and board[i][j-1] == "o" and board[i][j-2] == ".":
            count += 1
        if board[i][j] == "o" and i > 1 and board[i-1][j] == "o" and board[i-2][j] == ".":
            count += 1
        if board[i][j] == "o" and i < (len(board) - 2) and board[i+1][j] == "o" and board[i+2][j] == ".":
            count += 1
        if board[i][j] == "o" and j < (len(board[i]) - 2) and board[i][j+1] == "o" and board[i][j+2] == ".":
            count += 1
        j += 1
    i += 1
print(count)
