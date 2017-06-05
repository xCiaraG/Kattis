import sys
lines = sys.stdin.readlines()
i = 0
while i < len(lines):
	toGraph = []
	while i < len(lines) and lines[i] != "\n":
		toGraph.append(lines[i].strip())
		i += 1
	toGraph = toGraph[::-1]
	j = 0
	k = 0
	while j < len(toGraph):
		n = toGraph[j].count("*")
		tmp = "."*k + "*"*n + "."*(len(toGraph[j])-n-k)
		k += n
		toGraph[j] = tmp
		j += 1
	for p in toGraph[::-1]:
		print(p)
	i += 1
	if i < len(lines):
		print()


