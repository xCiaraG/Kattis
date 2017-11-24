n = int(input())
print("{}:".format(n))
for i in range(2, n):
	if (n % (i+(i-1)) == 0 or n % (i+(i-1)) == i):
		print("{},{}".format(i, i-1))
	if n % i == 0:
		print("{},{}".format(i, i))
