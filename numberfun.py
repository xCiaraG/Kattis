n = int(input())
for i in range(n):
	a, b, c = [int(x) for x in input().split()]
	if a + b == c or a - b == c or b - a == c or a*b == c or a/b == c or b/a == c:
		print("Possible")
	else:
		print("Impossible")