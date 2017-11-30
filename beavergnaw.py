import math
from sys import stdin
lines = stdin.readlines()
for line in lines[:-1]:
	D, V = [int(x) for x in line.split()]
	print((((D**3) - (6 * V) / math.pi))**(1/3))