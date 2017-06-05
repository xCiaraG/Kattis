n = input().strip()
degree = len(n)
x = 0
y = 0
i = 0
while i < len(n):
	if n[i] == "0":
		if x:
			x = 2*x
		if y:
			y = 2*y
	elif n[i] == "1":
		if x:
			x = 2*x
		if not y:
			y = 1
		else:
			y = 2*y + 1
	elif n[i] == "2":
		if not x:
			x = 1
		else:
			x = 2*x + 1
		if y:
			y = 2*y
	else:
		if not x:
			x = 1
		else:
			x = 2*x + 1
		if not y:
			y = 1
		else:
			y = 2*y + 1
	i += 1

print("{} {} {}".format(degree, y, x))