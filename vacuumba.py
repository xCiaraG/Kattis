import math
n = int(input())
for i in range(0, n):
	m = int(input())
	angle, x, y = 90, 0, 0
	for j in range(0, m):
		movement = [float(x) for x in input().split()]
		angle += movement[0] % 360
		distance = movement[1]
		x += math.cos(math.radians(angle))*distance
		y += math.sin(math.radians(angle))*distance
	print("{:.6f} {:.6f}".format(x, y))