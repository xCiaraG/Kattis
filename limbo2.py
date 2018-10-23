from sys import stdin

def find_next_power(n):
	i = 0
	while 2**i < n:
		i += 1
	return 2**i

n = int(stdin.readline())
for _ in range(n):
	r, c = [int(x) for x in stdin.readline().split()]
	next_pow = find_next_power(r + 1)
	if c < next_pow:
		print((next_pow * r) + c)
	else:
		next_pow = find_next_power(c + 1) // 2
		print((next_pow * (c - next_pow)) + r + (next_pow**2))
