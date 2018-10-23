def sum_first_n(n):
	return (n*(n + 1)) // 2

n = int(input())
for _ in range(n):
	l, r = [int(x) for x in input().split()]
	print(sum_first_n(l + r) + r + 1)