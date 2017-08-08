def gcd(a, b):
	if b > a:
		tmp = b
		b = a
		a = tmp
	while b != 0:
		tmp = a % b
		a = b
		b = tmp
	return a

def lcm(a, b):
	return (a*b)//gcd(a, b)

n = int(input())
for i in range(0, n):
	m = int(input().strip())
	wheels = [int(x) for x in input().split()]
	for i in range(1, m):
		wheels[i] = lcm(wheels[i-1], wheels[i])

	if wheels[-1] > 1000000000:
		print("More than a billion.")
	else:
		print(wheels[-1])