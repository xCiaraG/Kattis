from sys import stdin
n = int(stdin.readline())
for _ in range(n):
	m, s = stdin.readline().strip().split()
	l = len(s)
	m = int(m)
	if m > 24:
		m = 24
	for _ in range(m):
		l -= l/4
		s = s[::-1][:l]
	if m % 2 == 1:
		s = s[::-1]
	print(s)

