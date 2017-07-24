n = int(input().strip())
rectanges = []
circles = []
for i in range(0, n):
	line = input().strip().split()
	if line[0] == "circle":
		circles.append(list(map(int, line[1:])))
	else:
		rectanges.append(list(map(int, line[1:])))
n = int(input())
for i in range(0, n):
	count = 0
	point = list(map(int, input().strip().split()))
	for r in rectanges:
		if r[0] <= point[0] <= r[2] and r[1] <= point[1] <= r[3]:
			count += 1
	for c in circles:
		if ((c[0]-point[0])**2 + (c[1]-point[1])**2)**0.5 <= c[2]:
			count += 1
	print(count)
