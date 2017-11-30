from sys import stdin
a = int(stdin.readline())
for _ in range(a):
	n, m = [int(x) for x in stdin.readline().split()]
	for _ in range(m):
		x = stdin.readline()
	print(n-1)

