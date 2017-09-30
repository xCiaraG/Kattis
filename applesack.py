n, k = [int(x) for x in input().split()]
count = 0
while n > k:
	if n % k == 0:
		n -= n//k
	else:
		n -= n//k + 1
	count += 1
count += n
print(count+1)