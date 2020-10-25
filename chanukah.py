from sys import stdin
n = int(stdin.readline())
for i in range(n):
	a, b = [int(x) for x in stdin.readline().split()]
	print("{} {}".format(i + 1, ((b)*(b+1)//2) + b))