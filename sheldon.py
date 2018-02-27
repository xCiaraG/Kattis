numbers = []
for n in range(1, 64):
	numbers.append(int("1"*n, base=2))
	for i in range (1, n):
		for j in range(1, n):
			if n % (i+j) == 0:
				m = n // (i + j)
				numbers.append(int(("1"*i + "0"*j)*m, base=2))
			if j != 0 and (n - i) % (i + j) == 0:
				m = (n - i) // (i + j)
				numbers.append(int(("1"*i + "0"*j)*m + "1"*i, base=2))
x, y = [int(x) for x in input().split()]
total = 0
for n in numbers:
	if x <= n <= y:
		total += 1
print(total)