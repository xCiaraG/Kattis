import sys
from decimal import *
lines = sys.stdin.readlines()
for line in lines:
	line = list(map(int, line.strip().split()))
	getcontext().prec = line[2]+10
	l = line[2] + 1
	s = str(Decimal(line[0])/Decimal(line[1]))
	if len(s) < l + 1:
		s += "0"*(l-len(s) + 1)
	while len(s) > l + 1:
		s = s[:-1] 
	print(s)