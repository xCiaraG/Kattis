import math
def get_position(n):
	for i in range(3):
		for j in range(3):
			if keypad[i][j] == n:
				return i, j

keypad = []
for i in range(3):
	keypad.append([int(x) for x in input().split()])

t = 0
for i in range(1, 9):
	x1, y1 = get_position(i)
	x2, y2 = get_position(i+1)
	if x1 == x2:
		t += abs(y1-y2)
	elif y1 == y2:
		t += abs(x1-x2)
	else:
		t += math.sqrt((x1-x2)**2 + (y1-y2)**2)

print(t)