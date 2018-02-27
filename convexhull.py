from sys import stdin

def clockwise(p1, p2, p3):
	(x1, y1), (x2, y2), (x3, y3) = p1, p2, p3
	return ((x2-x1)*(y3-y1)) - ((y2-y1)*(x3-x1)) > 0

def convexhull(points):
	upperHull = [points[0], points[1]]
	lowerHull = [points[-1], points[-2]]

	for i in range(n - 2, -1, -1):
			while len(lowerHull) > 1 and not clockwise(points[i], lowerHull[-1], lowerHull[-2]):
				lowerHull.pop()
			lowerHull.append(points[i])

	for i in range(2, n):
		while len(upperHull) > 1 and not clockwise(points[i], upperHull[-1], upperHull[-2]):
			upperHull.pop()
		upperHull.append(points[i])

	convex_hull = upperHull + lowerHull[1:-1]
	convex_hull = convex_hull[::-1]
	if convex_hull[0] == convex_hull[-1]:
		convex_hull = convex_hull[1:]
	return convex_hull

n = int(stdin.readline())
while n != 0:
	points = []
	for i in range(n):
		x, y = [int(x) for x in stdin.readline().split()]
		points.append((x, y))
	points = sorted(points)
	
	if len(points) > 1:
		convex_hull = convexhull(points)
	else:
		convex_hull = points
		
	print(len(convex_hull))
	for x, y in convex_hull:
		print x, y
	n = int(stdin.readline())

