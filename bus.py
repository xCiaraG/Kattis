n = int(input())
for i in range(0, n):
	m = int(input())
	ans = 1
	for j in range(1, m):
		ans += ans + 1
	print(ans)