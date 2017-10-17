from math import pi
x, y = [float(x) for x in input().split()]
if (y**2)/(4*pi) >= x:
	print("Diablo is happy!")
else:
	print("Need more materials!")