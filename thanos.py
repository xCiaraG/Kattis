from sys import stdin
n = int(stdin.readline())
for _ in range(n):
	p, r, f = [int(x) for x in stdin.readline().split()]
	total = 0
	while p <= f:
		p *= r
		total += 1
	print(total)