n = int(input())
buildings = [int(x) for x in input().split()]
buildings = sorted(buildings)[::-1]
total = min(buildings[0], n)
i = 1
while i < n:
	if i + buildings[i] < total:
		total = i + buildings[i]
	i += 1
print(total)
