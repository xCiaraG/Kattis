import math
n = int(input())
for i in range(0, n):
	num = int(input()) 
	print(int((math.factorial(2*num))//(math.factorial(num+1)*(math.factorial(num)))))