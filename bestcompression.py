n, b = [int(x) for x in input().split()]
if 2**(b+1) - 1 >= n:
	print("yes")
else:
	print("no")