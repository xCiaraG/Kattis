import math
n = int(input())
for i in range(0, n):
	m = int(input())
	angle = 90
	x, y = 0.0, 0.0
	for j in range(0, m):
		cmd = input().split()
		d = int(cmd[1])
		if cmd[0] == "fd":
			x += d*math.cos(math.radians(angle))
			y += d*math.sin(math.radians(angle))
		elif cmd[0] == "bk":
			x -= d*math.cos(math.radians(angle))
			y -= d*math.sin(math.radians(angle))
		elif cmd[0] == "rt":
			angle = (angle + d) % 360
		else:
			angle = (angle - d) % 360
	print(round(math.hypot(x, y)))