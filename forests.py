from sys import stdin
from collections import defaultdict
n, _ = [int(x) for x in stdin.readline().split()]
people = defaultdict(list)
for line in stdin.readlines():
	i, j = [int(x) for x in line.split()]
	people[i].append(j)
ans = set()
for k in range(1, n+1):
	ans.add("-".join(str(x) for x in sorted(people[k])))
print(len(ans))