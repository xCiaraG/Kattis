import math
try:
	n = int(input())
	m = n
	total = 0
	while m != 1 and m != 0:
		total += (math.factorial(n))/(math.factorial(m)*(math.factorial(n-m)))	
		m -= 1
except:
	pass

print(int(total))