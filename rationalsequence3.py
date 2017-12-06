n = int(input())
for i in range(n):
	k, p = [int(x) for x in input().split()]
	num, den = 1, 1
	for c in bin(p)[3:]:
		if c == "0":
			den += num
		else:
			num += den
	print("{} {}/{}".format(k, num, den))