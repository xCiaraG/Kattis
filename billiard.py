import math
line = [int(x) for x in input().split()]
while line != [0, 0, 0, 0, 0]:
	x = line[0]*line[3]
	y = line[1]*line[4]
	d = math.sqrt(x**2 + y**2)
	v = d/line[2]
	if x != 0:
		a = math.degrees(math.atan(y/x))
	else:
		a = 90

	print("{:.2f} {:.2f}".format(a, v))
	line = [int(x) for x in input().split()]