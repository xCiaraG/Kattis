from sys import stdin

def check_possible(x1, y1, x2, y2):
	return (x1 + y1 + x2 + y2) % 2 == 0

def find_moves(x1, y1, x2, y2):
	moves = [[(x1, y1)]]
	while True:
		current = moves.pop(0)
		x, y = current[-1]
		if x == x2 and y == y2:
			return current
		for i in range(1, 9):
			for (a, b) in [(i, i), (-i, -i), (-i, i), (i, -i)]:
				tmpx, tmpy = a + x, b + y
				if 0 < tmpx <= 8 and 0 < tmpy <= 8:
					moves.append(current + [(tmpx, tmpy)])
letter_to_num = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
nums_to_letter = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H'}
n = int(stdin.readline())
for _ in range(n):
	x1, y1, x2, y2 = [x for x in stdin.readline().strip().split()]
	x1 = letter_to_num[x1]
	y1 = int(y1)
	x2 = letter_to_num[x2]
	y2 = int(y2)
	if not check_possible(x1, y1, x2, y2):
		print('Impossible')
	else:
		moves = find_moves(x1, y1, x2, y2)
		ans = str(len(moves) - 1)
		for a, b in moves:
			ans += ' {} {}'.format(nums_to_letter[a], b)
		print(ans)

