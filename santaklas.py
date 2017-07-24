import math
line = list(map(int, input().strip().split()))
if 0 <= line[1] <= 180:
	print("safe")
elif line[1] <= 270:
	a = line[1] - 180
	a = 90 - a
	if a == 0:
		print(line[0])
	else:
		print(int(line[0]/math.cos(math.radians(a))))
else:
	a = line[1] - 270
	if a == 90:
		print(line[0])
	else:
		print(int(line[0]/math.cos(math.radians(a))))