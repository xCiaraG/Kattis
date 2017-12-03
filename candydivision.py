def find_divisors(n):
	divisors = []
	maxi = int(n**(0.5)+1)
	for i in range(1, maxi+1):
		if n % i == 0:
			divisors.append(i)
			divisors.append(n//i)
	return sorted(list(set(divisors)))

n = int(input())
print(*[x - 1 for x in find_divisors(n)])