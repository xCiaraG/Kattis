import math

def distance(x1, y1, x2, y2):
	return math.sqrt((x2-x1)**2 + (y2-y1)**2)

n = int(input().strip())
for i in range(0, n):
	m = int(input().strip())
	colours = []
	for j in range(0, m):
		splat = input().split()
		colours.append(((float(splat[0])), float(splat[1]), math.sqrt(float(splat[2])/math.pi), splat[3]))
	colours = colours[::-1]
	m = int(input().strip())
	for j in range(0, m):
		point = [float(x) for x in input().split()]
		k = 0
		while k < len(colours):
			d = distance(point[0], point[1], colours[k][0], colours[k][1])
			if d <= colours[k][2]:
				print(colours[k][3])
				break
			k += 1
		if k == len(colours):
			print("white")