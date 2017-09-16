from sys import stdin
n = int(stdin.readline())
for i in range(0, n):
	r, e, c = [int(x) for x in stdin.readline().split()]
	if e - r == c:
		print("does not matter")
	elif e - r < c:
		print("do not advertise")
	else:
		print("advertise")