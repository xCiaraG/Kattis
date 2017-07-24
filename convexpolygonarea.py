n = int(input())
for i in range(0, n):
	line = list(map(int, input().strip().split()))
	points = []
	j = 1
	while j + 1 < len(line):
		points.append((line[j], line[j+1]))
		j += 2
	points.append(points[0])
	j, x, y = 0, 0, 0
	while j + 1 < len(points):
		x += (points[j][0]*points[j+1][1])
		y += (points[j][1]*points[j+1][0])
		j += 1
	ans = .5*abs((y-x))
	if ans % 1 == 0:
		print(int(ans))
	else:
		print(ans)
