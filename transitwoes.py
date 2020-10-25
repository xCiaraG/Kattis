from sys import stdin

s, t, n = [int(x) for x in stdin.readline().split()]
d = [int(x) for x in stdin.readline().split()]
b = [int(x) for x in stdin.readline().split()]
c = [int(x) for x in stdin.readline().split()]
total = s 
for i in range(n):
	total += d[i]
	if total % c[i] != 0:
		total += c[i] - (total % c[i])
	total += b[0]
total += d[-1]
if total <= t:
	print("yes")
else:
	print("no")
