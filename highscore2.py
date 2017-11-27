n = int(input())
for _ in range(n):
	a, b, c, d = [int(x) for x in input().split()]
	a, b, c = sorted((a, b, c))
	maxi = a**2 + b**2 + (c+d)**2 + a*7
	i = 0
	while d != 0 and i < 100:
		a += 1
		d -= 1
		a, b, c = sorted((a, b, c))
		current = a**2 + b**2 + (c+d)**2 + a*7
		if current > maxi:
			maxi = current
		i += 1
	print(maxi)