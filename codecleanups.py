def dirtiness(l, d):
	total = 0
	for n in l:
		total += (d - n)
	return total

n = int(input())
numbers = [int(x) for x in input().split()]
cleanups = 0
current = []
for i in range(395):
	if i in numbers:
		current.append(i)
	if dirtiness(current, i) > 19:
		cleanups += 1
		if i in current:
			current = [i]
		else:
			current = []
print(cleanups)
