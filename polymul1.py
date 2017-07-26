from sys import stdin
n = int(input())
for i in range(0, n):
	d1 = int(stdin.readline())
	p1 = [int(x) for x in stdin.readline().split()]
	d2 = int(stdin.readline())
	p2 = [int(x) for x in stdin.readline().split()]
	p3 = [0]*(d1+d2+1)
	p1 = p1[::-1]
	p2 = p2[::-1]
	j = 0
	while j < d1+1:
		k = 0
		while k < d2+1:
			p3[j+k] += (p1[j] * p2[k])
			k += 1
		j += 1
	print(d1+d2)
	print(" ".join(map(str, p3[::-1])))
