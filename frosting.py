from sys import stdin
n = int(stdin.readline())
a = [int(x) for x in stdin.readline().split()]
b = [int(x) for x in stdin.readline().split()]

sums = [0, 0, 0]
areas = [0, 0, 0]

for i in range(n):
	sums[i % 3] += b[i]

for i in range(n):
   areas[0] += sums[0] * a[i]
   areas[1] += sums[1] * a[i]
   areas[2] += sums[2] * a[i]
   tmp = sums.pop()
   sums = [tmp] + sums

tmp = areas.pop(0)
areas.append(tmp)
print(*areas)