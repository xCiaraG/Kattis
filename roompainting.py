from sys import stdin
n, m = [int(x) for x in stdin.readline().split()]
buckets, needed = [0]*n, [0]*m

for i in range(0, n):
	num = int(stdin.readline())
	buckets[i] = num

for i in range(0, m):
	num = int(stdin.readline())
	needed[i] = num

buckets, needed = sorted(buckets), sorted(needed)
needed.append(buckets[-1]+1)

i, j, t = 0, 0, 0
while i < m:
	tmp = needed[i]
	while buckets[j] < tmp:
		j += 1	
	tmp = buckets[j]
	while needed[i] <= tmp:
		t += buckets[j] - needed[i]
		i += 1

print(t)