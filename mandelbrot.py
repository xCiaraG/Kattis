import math, sys
lines = sys.stdin.readlines()
i = 1
for line in lines:
	line = list(map(float, line.strip().split()))
	x = line[0]
	y = line[1]
	k = 1
	iterations = int(line[2])
	while k < iterations and (math.sqrt(x**2 + y**2) < 2):
		tmpx = x
		x = (x**2 - y**2)+line[0]
		y = 2*tmpx*y + line[1]
		k += 1
	if math.sqrt(x**2 + y**2) >= 2:
		print("CASE {}: OUT".format(i))
	else:
		print("CASE {}: IN".format(i))
	i += 1