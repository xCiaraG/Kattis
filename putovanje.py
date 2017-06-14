line = list(map(int, input().strip().split()))
c = line[1]
fruit = list(map(int, input().strip().split()))
max_different_fruit = 0
i = 0
while i < len(fruit):
	j = i
	current_max = 0
	total = 0
	while total < c and j < len(fruit):
		if fruit[j] + total <= c:
			total += fruit[j]
			current_max += 1
		j += 1
	if current_max > max_different_fruit:
		max_different_fruit = current_max
	i += 1
print(max_different_fruit)


