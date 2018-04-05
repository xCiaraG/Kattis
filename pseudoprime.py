from sys import stdin
from math import sqrt
def is_prime(n):
    for i in range(2, int(sqrt(n))):
    	if n % i == 0:
    		return False
    return True

p, a = [int(x) for x in stdin.readline().split()]
while p != 0 and a != 0:
	if pow(a, p, p) == a and not is_prime(p):
		print("yes")
	else:
		print("no")
	p, a = [int(x) for x in stdin.readline().split()]