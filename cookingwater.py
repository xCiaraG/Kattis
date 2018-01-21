n = int(input())
minx, maxy = [int(j) for j in input().split()]
for i in range(n - 1):
	x, y = [int(j) for j in input().split()]
	if x > minx:
		minx = x
	if y < maxy:
		maxy = y
if minx <= maxy:
	print("gunilla has a point")
else:
	print("edward is right")
