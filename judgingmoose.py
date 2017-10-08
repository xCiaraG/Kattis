x, y = [int(x) for x in input().split()]
if x == 0 and y == 0:
	print("Not a moose")
elif x == y:
	print("Even {}".format(x + y))
else:
	print("Odd {}".format(max(x, y)*2))