n = int(input())
for i in range(n):
	m, k = input().split()
	if "9" not in k and "8" not in k:
		base8 = int(k, base=8)
	else:
		base8 = 0 
	print("{} {} {} {}".format(m, base8, int(k), int(k, base=16)))