from sys import stdin
y, p = stdin.readline().split()
if y.endswith("ex"):
	print(y + p)
elif y.endswith("e"):
	print(y + "x" + p)
elif y[-1] in "aiou":
	print(y[:-1] + "ex" + p)
else:
	print(y + "ex" + p)