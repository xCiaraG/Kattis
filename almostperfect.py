from sys import stdin

def find_divisors(n):
	divisors = []
	maxi = int(n**(0.5)+1)
	for i in range(1, maxi+1):
		if n % i == 0:
			divisors.append(i)
			divisors.append(n//i)
	return sorted(list(set(divisors)))

def type_perfect(n):
	m = sum(find_divisors(n)) - n
	if m == n:
		return "perfect"
	elif m - 2 <= n <= m + 2:
		return "almost perfect"
	else:
		return "not perfect"

numbers = stdin.readlines()
for n in numbers:
	n = int(n)
	print("{} {}".format(n, type_perfect(n)))
