from math import sqrt
from sys import stdin

def dist(x1, y1, x2, y2):
	return sqrt((y2 - y1)**2 + (x2 - x1)**2)

def get_primes(n):
    table = [True]*n
    primes = [2]*(n//2)
    count = 1                   
    for p in range(3, n, 2):
        if table[p]:    
            primes[count] = p
            count += 1
            for m in range(p*3, n, p*2):
                table[m] = False
    return primes[:count]

primes = get_primes(20100)
n = int(stdin.readline())
for _ in range(n):
	x1, y1 = 0, 0
	count, current_distance = 0, 0
	m, max_distance = [int(x) for x in stdin.readline().split()]
	for _ in range(m):
		x2, y2 = [int(x) for x in stdin.readline().split()]
		if current_distance < max_distance:
			d = dist(x1, y1, x2, y2)
			if current_distance + d <= max_distance:
				count += 1
				current_distance += d
			else:
				current_distance = max_distance
		x1, y1 = x2, y2
	i = 0
	while primes[i] <= count:
		i += 1
	if i == 0:
		print(0)
	else:
		print(primes[i - 1])
