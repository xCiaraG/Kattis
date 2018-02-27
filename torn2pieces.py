from collections import defaultdict
n = int(input())
connections = defaultdict(set)
for i in range(n):
	station = input().split()
	a = station[0]
	for b in station[1:]:
		connections[a].add(b)
		connections[b].add(a)
start, destination = input().split()
visited = set([start])
to_check = [(c, [start, c]) for c in connections[start]]
while to_check and destination != to_check[0][0]:
	current_station, current_route = to_check.pop(0)
	if current_station not in visited:
		visited.add(current_station)
		for c in connections[current_station] - visited:
			to_check.append((c, current_route + [c]))
if to_check:
	print(" ".join(to_check[0][1]))
else:
	print("no route found")




