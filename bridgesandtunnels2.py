from sys import stdin
from collections import defaultdict
from heapq import heappush, heappop

def find_shortest_path(paths, start, end):
	seen = set()
	to_check = [[0, 0, start]]
	while to_check:
		total_outside, total, orig = heappop(to_check)
		if orig in seen:
			continue
		seen.add(orig)
		if orig == end:
			return "{} {}".format(total_outside, total)
		for dest, time, outside in paths[orig]:
			if dest not in seen:
				time_outside = total_outside
				if outside == "O":
					time_outside += time
				heappush(to_check, [time_outside, total + time, dest])
	return "IMPOSSIBLE"

n, m, p = [int(x) for x in stdin.readline().split()]
paths = defaultdict(list)

for _ in range(m):
	orig, dest, time, outside = [x for x in stdin.readline().split()]
	paths[int(orig)].append([int(dest), int(time), outside])
	paths[int(dest)].append([int(orig), int(time), outside])

for _ in range(p):
	start, end =[int(x) for x in stdin.readline().split()]
	print(find_shortest_path(paths, start, end))
