n = int(input())
for i in range(0, n):
	word = input().strip()
	so_far = input().strip()
	prediction1 = input().strip()
	prediction2 = input().strip()
	prediction3 = input().strip()
	m = len(so_far) * len(word)
	total = 0
	if len(so_far) > len(word):
		total += len(so_far) - len(word)
		so_far = so_far[:len(word)]
	while word[:len(so_far)] != so_far:
		so_far = so_far[:-1]
		total += 1
	total += len(word) - len(so_far)
	if total < m:
		m = total
	for p in [prediction1, prediction2, prediction3]:
		total = 1
		if len(p) > len(word):
			total += len(p) - len(word)
			p = p[:len(word)]
		while word[:len(p)] != p:
			p = p[:-1]
			total += 1
		total += len(word) - len(p)
		if total < m:
			m = total
	print(m)