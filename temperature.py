line = [int(x) for x in input().split()]
x = line[0]
y = line[1]
if x == 0 and y == 1:
	print("ALL GOOD")
elif y == 1:
	print("IMPOSSIBLE")
elif x % (1-y) == 0:
	print(x//(1-y))
else:
	print(x/(1-y))