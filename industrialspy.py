from itertools import permutations, combinations
from sys import stdin
def get_primes(n):
    table = [0, 0, 1] + [1, 0]*((n-2)//2)
    for p in range(3, int(n**(0.5)) + 1, 2):
        if table[p]:    
            for m in range(p*2, n, p):
                table[m] = 0
    return table

primes = get_primes(9999999)
primes = set([i for i in range(0, len(primes)) if primes[i]])

n = int(stdin.readline().strip())
for _ in range(n):
	line = stdin.readline().strip()
	nums = set([int(x) for x in line])
	for i in range(2, len(line) + 1):
		for x in set(combinations(line, i)):
			nums = nums.union(set([int("".join(y)) for y in permutations(x)]))
	count = 0
	for p in nums:
		if p in primes:
			count += 1
	print(count)