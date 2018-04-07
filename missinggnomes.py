n, m = [int(x) for x in input().split()]
numbers = set()
order = []
for _ in range(m):
	tmp = int(input())
	numbers.add(tmp)
	order.append(tmp)
to_place = [i for i in range(1, n + 1) if i not in numbers]

i, j = 0, 0
while i < len(order) and j < len(to_place):
	if order[i] < to_place[j]:
		print(order[i])
		i += 1
	else:
		print(to_place[j])
		j += 1

while i < len(order):
	print(order[i])
	i += 1

while j < len(to_place):
	print(to_place[j])
	j += 1
