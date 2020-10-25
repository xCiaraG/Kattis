from sys import stdin

n, q = [int(x) for x in stdin.readline().split()]
locations = [int(x) for x in stdin.readline().split()]
d = dict()
for i in range(1, n+1):
	d[i] = locations[i-1]
for _ in range(q):
	t, a, b = [int(x) for x in stdin.readline().split()]
	if t == 1:
		d[a] = b
	else:
		print(abs(d[a] - d[b]))
