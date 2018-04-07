n, k = [int(x) for x in input().split()]
n -= 1
current = 0
count = 0
if k > n:
	print(n)
else:
	current = k
	count = k
	if n//k != 1:
		count += 1
		current = k * (n//k)
	print(count + n - current)
