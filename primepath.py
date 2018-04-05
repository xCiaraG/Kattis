from sys import stdin
def get_primes(n):
    table = [0, 0, 1] + [1, 0]*((n-2)//2)
    for p in range(3, int(n**(0.5)) + 1, 2):
        if table[p]:    
            for m in range(p*2, n, p):
                table[m] = 0
    return table

def bfs(primes, s, p):
	to_check = [(s, 0)]
	seen = set()
	while to_check:
		current, count = to_check.pop(0)
		if current in primes and current not in seen:
			seen.add(current)
			if current == p:
				return count
			for i in "0123456789":
				tmp = i + current[1:]
				if tmp in primes:
					to_check.append((tmp, count + 1))
				tmp = current[0] + i + current[2:]
				if tmp in primes:
					to_check.append((tmp, count + 1))
				tmp = current[:2] + i + current[3:]
				if tmp in primes:
					to_check.append((tmp, count + 1))
				tmp = current[:3] + i
				if tmp in primes:
					to_check.append((tmp, count + 1))
	return "Impossible"

primes = get_primes(10000)
primes = set([str(i) for i in range(0, len(primes)) if primes[i] and 1000 < i < 10000])
n = int(stdin.readline())
for i in range(n):
	p1, p2 = [x for x in stdin.readline().split()]
	print(bfs(primes, p1, p2))