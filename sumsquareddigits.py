from sys import stdin

def compute(num, base):
	res = 0
	while num:
		res += (num % base)**2
		num //= base
	return res

n = int(stdin.readline())
for _ in range(n):
	k, base, num = [int(x) for x in stdin.readline().split()]
	print("{} {}".format(k, compute(num, base)))
