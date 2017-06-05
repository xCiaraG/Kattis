import sys
def find_pos(letter, puzzle):
	i = 0
	while i < len(puzzle):
		j = 0
		while j < len(puzzle[i]):
			if letter == puzzle[i][j]:
				return i, j
			j += 1
		i += 1

puzzle = []
p = ["ABCD", "EFGH", "IJKL", "MNO "]
lines = sys.stdin.readlines()
for line in lines:
	puzzle.append(line)

total = 0
i = 0
while i < len(p):
	j = 0
	while j < len(p[0]):
		if p[i][j] != puzzle[i][j] and p[i][j] != " ":
			x1, y1 = find_pos(p[i][j], puzzle)
			total += abs(i - x1) + abs(j - y1)
		j += 1
	i += 1
print(total)

