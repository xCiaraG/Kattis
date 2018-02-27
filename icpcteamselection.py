n = int(input())
for i in range(n):
	m = int(input())
	teams = sorted([int(x) for x in input().split()])
	total = 0
	while teams:
		teams.pop(0)
		teams.pop()
		total += teams.pop()
	print(total)