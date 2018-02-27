from sys import stdin
from math import sqrt
n = int(stdin.readline())
while n != 0:
	if n < 3 or 4 <= n <= 6:
		print("No such base")
	else:
		i = 4
		n -= 3
		end = sqrt(n)
		tmp = 0
		if n % 2 == 0:
			tmp = n // 2
		if n % 3 == 0:
			tmp = n // 3
		while n % i != 0 and i < end:
			i += 1

		if n % i == 0:
			print(i)
		elif tmp and tmp >= 4:
			print(tmp)
		else:
			print(n)
	n = int(stdin.readline())