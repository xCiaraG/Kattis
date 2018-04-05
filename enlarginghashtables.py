from math import sqrt
def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
    	if n % i == 0:
    		return False
    return True

def find_prime(n):
	while not is_prime(n):
		n += 1
	return n

n = input()
while n != 0:
	ans = find_prime(2*n + 1)
	if not is_prime(n):
		print("{} ({} is not prime)".format(ans, n))
	else:
		print(ans)
	n = input()