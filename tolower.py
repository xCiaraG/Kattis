count = 0
n, m = [int(x) for x in input().strip().split()]
for i in range(n):
	ans = True
	for j in range(m):
		tmp = input().strip()
		if tmp.lower() != tmp[0].lower() + tmp[1:]:
			ans	= False
	if ans:
		count += 1
print(count)