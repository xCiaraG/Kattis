from sys import stdin
n, m = [int(x) for x in stdin.readline().split()]
tasks = sorted([int(x) for x in stdin.readline().split()], reverse=True)
intervals = sorted([int(x) for x in stdin.readline().split()], reverse=True)
count = 0
i = 0
for task in tasks:
	if i < m and task <= intervals[i]:
		count += 1
		i += 1
print(count)