n = int(input())
x, y = 0, 0
if (n - 2) % 4 == 0:
	print("impossible")
else:
	while y**2 - x**2 != n:
		if y**2 - x**2 > n:
			x += 1
		else:
			y += 1
	print(x, y)