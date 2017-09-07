from sys import stdin

def gcd(a, b):
	if b > a:
		a, b = b, a
	while b != 0:
		a, b = b, a % b
	return a

def lcm(a, b):
	return (a*b)//gcd(a, b)

lines = stdin.readlines()
for line in lines:
	line = map(int, line.split())
	m = line[0]
	for n in line[1:]:
		m = lcm(m, n)
	print(m)

	

