from sys import stdin
n = int(stdin.readline())
ans = [0]*365
for _ in range(n):
	a, b = [int(x) for x in stdin.readline().split()]
	for i in range(a-1, b):
		ans[i] = 1
print(sum(ans))