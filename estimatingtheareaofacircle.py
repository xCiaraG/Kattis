import math
line = list(map(float, input().strip().split()))
while line != [0, 0, 0]:
	print("{} {}".format(math.pi*line[0]**2, ((line[2]/line[1] * 4)* line[0]**2)))
	line = list(map(float, input().strip().split()))
