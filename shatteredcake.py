from sys import stdin
w = int(stdin.readline())
n = int(stdin.readline())
area = 0
for i in range(n):
	a, b = [int(x) for x in stdin.readline().split()]
	area += (a*b)

print(area//w)