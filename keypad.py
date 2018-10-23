from sys import stdin

def check_possible(grid, r, c):
	rows = set()
	columns = set()
	for i in range(r):
		for j in range(c):
			if grid[i][j] == '1':
				rows.add(i)
				columns.add(j)
	new_grid = []
	for i in range(r):
		current = ''
		for j in range(c):
			if i in rows and j in columns:
				current += '1'
			else:
				current += '0'
		new_grid.append(current)
	return grid == new_grid

def check_double(grid, i, j, r):
	if grid[i].count('1') == 1:
		return False
	else:
		count = 0
		for x in range(r):
			if grid[x][j] == '1':
				count += 1
		if count == 1:
			return False
	return True

n = int(stdin.readline())
for _ in range(n):
	r, c = [int(x) for x in stdin.readline().split()]
	grid = [stdin.readline().strip() for _ in range(r)]
	if not check_possible(grid, r, c):
		print('impossible')
	else:
		ans = []
		for i in range(r):
			current = ''
			for j in range(c):
				tmp = grid[i][j] 
				if tmp == '0':
					current += 'N'
				elif check_double(grid, i, j, r):
					current += 'I'
				else:
					current += 'P'
			ans.append(current)
		for line in ans:
			print(line)
	print('----------')