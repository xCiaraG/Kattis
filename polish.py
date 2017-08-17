from sys import stdin

def add(x1, x2):
	return str(int(x2) + int(x1))

def subtract(x1, x2):
	return str(int(x2) - int(x1))

def multiply(x1, x2):
	return str(int(x2) * int(x1))

lines = stdin.readlines()
c = 0
for line in lines:
	c += 1
	to_solve = line.split()[::-1]
	i = 0
	while i + 2 < len(to_solve):
		if to_solve[i][-1] in "0123456789" and to_solve[i+1][-1] in "0123456789" and to_solve[i+2] in "+*-":
			if to_solve[i+2] == "+":
				tmp = add(to_solve[i], to_solve[i+1])
			elif to_solve[i+2] == "-":
				tmp = subtract(to_solve[i], to_solve[i+1])
			else:
				tmp	= multiply(to_solve[i], to_solve[i+1]) 
			to_solve[i] = tmp
			to_solve = to_solve[:i+1] + to_solve[i+3:]
			i = 0
		else:
			i += 1
	print("Case {}: {}".format(c, " ".join(to_solve[::-1])))

