import math

def calculate_dist(l, capacity):
	total, current = 0, 0
	c = capacity
	for location, letters in sorted(l, reverse=True):
		total += abs(current - location)
		if letters - c > 0:
			letters -= c
			total += math.ceil(letters/capacity)*location*2
			c = (capacity - letters) % capacity
		else:
			c -= letters
		current = location
	return total + current

n, capacity = [int(x) for x in input().split()]
above = []
below = []
for _ in range(n):
	location, letters = [int(x) for x in input().split()]
	if location < 0:
		below.append((abs(location), letters))
	else:
		above.append((location, letters))

print(calculate_dist(above, capacity) + calculate_dist(below, capacity))

