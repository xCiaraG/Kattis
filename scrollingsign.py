n = int(input())
for i in range(n):
	k, w = [int(x) for x in input().split()]
	count = k
	current = input().strip()
	for i in range(w-1):
		tmp = input().strip()
		j = 0
		while j < k:
			if current[j:] == tmp[:k-j]:
				break
			j += 1
		count += k - (k - j)
		current = tmp
	print(count)
