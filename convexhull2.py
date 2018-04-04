from sys import stdin

def clockwise(p1, p2, p3):
	(x1, y1), (x2, y2), (x3, y3) = p1, p2, p3
	return ((x2-x1)*(y3-y1)) - ((y2-y1)*(x3-x1)) >= 0

def convexhull(points):
	convex_hull = [points[0], points[1]]
	for i in range(2, n):
		while len(convex_hull) > 1 and not clockwise(points[i], convex_hull[-1], convex_hull[-2]):
			convex_hull.pop()
		convex_hull.append(points[i])
	m = len(convex_hull)
	convex_hull.append(points[-2])
	tmp = set(convex_hull)
	for i in range(n - 1, -2, -1):
		while len(convex_hull) > m and not clockwise(points[i], convex_hull[-1], convex_hull[-2]):
			convex_hull.pop()
		if points[i] not in tmp:
			convex_hull.append(points[i])
	convex_hull = convex_hull[::-1]
	while min(convex_hull) != convex_hull[0]:
		convex_hull = [convex_hull[-1]] + convex_hull[:-1]
	return convex_hull

n = int(stdin.readline())
points = []
for i in range(n):
	line = stdin.readline().strip().split()
	if line[-1] == "Y":
		points.append((int(line[0]), int(line[1])))
points = sorted(points)
n = len(points)
if len(points) > 1:
	convex_hull = convexhull(points)
else:
	convex_hull = points
print(len(convex_hull))
for x, y in convex_hull:
	print x, y

