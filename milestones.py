times = [int(x) for x in input().split()]
passed = [int(x) for x in input().split()]
stones = [int(x) for x in input().split()]

stone_intervals = [stones[i] - stones[i-1] for i in range(1, times[1])]
passing_intervals = [passed[i] - passed[i-1] for i in range(1, times[0])]
results = []
i = 0
while i < times[1]-times[0]+1:
	j = 0
	ratio1 = stone_intervals[i]/passing_intervals[0]
	ratio = ratio1
	first = stone_intervals[i] 
	while j < times[0]-1 and ratio == ratio1:
		ratio1 = stone_intervals[i+j]/passing_intervals[j]
		j += 1
	if ratio1 == ratio:
		results.append(first)
	i += 1
results = sorted(set(results))
print(len(results))
print(*results)


