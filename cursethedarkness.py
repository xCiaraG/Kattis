import math
def distance(x1, y1, x2, y2):
	return math.sqrt(((x2-x1)**2)+((y2-y1)**2))

n = int(input())
for i in range(0, n):
	line = list(map(float, input().strip().split()))
	x1, y1 = line[0], line[1]
	m = int(input())
	a = False
	for j in range(0, m):
		line = list(map(float, input().strip().split()))
		x2, y2 = line[0], line[1]
		if distance(x1, y1, x2, y2) <= 8:
			a = True
	if a:
		print("light a candle")
	else:
		print("curse the darkness")