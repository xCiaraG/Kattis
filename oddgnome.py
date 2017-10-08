n = int(input())
for _ in range(n):
	gnomes = [int(x) for x in input().split()]
	i = 2
	while i < gnomes[0]:
		if (gnomes[i-1] >= gnomes[i] or gnomes[i+1] <= gnomes[i]) and sorted(gnomes[1:i] + gnomes[i+1:]) == (gnomes[1:i] + gnomes[i+1:]):
			print(i)
			i = gnomes[0]
		i += 1



