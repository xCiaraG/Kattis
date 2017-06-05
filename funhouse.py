def goDown(x, y, house):
	x += 1
	while house[x][y] not in "\/x":
		x += 1
	if house[x][y] == "/":
		return goleft(x, y, house)
	elif house[x][y] == "x":
		return x, y
	else:
		return goRight(x, y, house)

def goUp(x, y, house):
	x -= 1
	while house[x][y] not in "\/x":
		x -= 1
	if house[x][y] == "/":
		return goRight(x, y, house)
	elif house[x][y] == "x":
		return x, y
	else:
		return goleft(x, y, house)

def goRight(x, y, house):
	y += 1
	while house[x][y] not in "\/x":
		y += 1
	if house[x][y] == "/":
		return goUp(x, y, house)
	elif house[x][y] == "x":
		return x, y
	else:
		return goDown(x, y, house)

def goleft(x, y, house):
	y -= 1
	while house[x][y] not in "\/x":
		y -= 1
	if house[x][y] == "/":
		return goDown(x, y, house)
	elif house[x][y] == "x":
		return x, y
	else:
		return goUp(x, y, house)

def findStart(house):
	i = 0
	while i < len(house):
		j = 0
		while j < len(house[i]):
			if house[i][j] == "*":
				return i, j
			j += 1
		i += 1

def findExit(x, y, house):
	if x == 0:
		return goDown(x, y, house)
	elif x == len(house) - 1:
		return goUp(x, y, house)
	elif y == 0:
		return goRight(x, y, house)
	else:
		return goleft(x, y, house)

n = list(map(int, input().strip().split()))
k = 0
while n != [0, 0]:
	k += 1
	house = []
	for i in range(0, n[1]):
		house.append(input().strip())
	x, y = findStart(house)
	x, y = findExit(x, y, house)
	house[x] = house[x][:y] + "&" + house[x][y+1:]
	print("HOUSE {}".format(k))
	for wall in house:
		print(wall)
	n = list(map(int, input().strip().split()))