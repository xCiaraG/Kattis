import fractions
n = int(input())
for i in range(0, n):
	line = input().strip().split()
	x = fractions.Fraction(int(line[0]), int(line[1]))
	y = fractions.Fraction(int(line[3]), int(line[4]))
	op = line[2]
	if op == "+":
		z = x + y
	elif op == "-":
		z = x - y
	elif op == "*":
		z = x * y
	elif op == "/":
		z = x / y

	print("{} / {}".format(z.numerator, z.denominator))