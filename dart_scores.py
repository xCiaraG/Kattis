import math
n = int(input())
for i in range(0, n):
	m = int(input())
	total = 0
	for j in range(0, m):
		line = list(map(int, input().strip().split()))
		distance = ((line[0])**2+(line[1])**2)**(1/2)
		if distance % 20 != 0:
			distance = distance//20 + 1
		else:
			distance = distance//20
		if distance <= 10:
			if distance == 0:
				distance = 1
			total += 11-distance
	print(int(total))
