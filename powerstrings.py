from sys import stdin

def find_divisors(n):
	divisors = []
	maxi = int((n**(0.5)+1))
	for i in range(1, maxi+1):
		if n % i == 0:
			divisors.append(i)
			divisors.append(n//i)
	return sorted(list(set(divisors)))

line = stdin.readline().strip()
while line != ".":
	length = len(line)
	divisors = find_divisors(length)
	for n in divisors:
		if line[-n:]*(length//n) == line:
			ans = (length//n)
			break
	print(ans)
	line = stdin.readline().strip()


