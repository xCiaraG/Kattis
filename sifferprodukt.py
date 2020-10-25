from sys import stdin

def digit_product(num):
	total = 1
	for n in num:
		if (int(n)):
			total *= int(n)
	return total

n = int(stdin.readline())
while n > 9:
	n = digit_product(str(n))
print(n)