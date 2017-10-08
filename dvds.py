from sys import stdin
n = int(input())
for i in range(0, n):
	m = int(input())
	t = 0
	current = 1
	order = [int(x) for x in stdin.readline().split()]
	for i in range(m):
		if order[i] != current:
			t += 1
		else:
			current += 1
	print(t)