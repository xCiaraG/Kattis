import sys, math
lines = sys.stdin.readlines()
for line in lines:
	line = list(map(float, line.strip().split()))
	r = line[0]
	x = line[1]
	y = line[2]
	d = ((x)**2+(y)**2)**0.5
	if d <= r:
		h = r - d
		area = math.pi*r**2
		area1 = (r**2)*(math.acos((r-h)/r))-(r-h)*(((2*r*h)-(h**2))**0.5)
		area2 = area - area1
		if area2 > area1:
			print(area2, area1)
		else:
			print(area1, area2)
	else:
		print("miss")