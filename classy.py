'''
d = {"middle": "aa", "upper": "a", "lower": "aaa"}
def getOrder(x):
	if x in d:
		return d[x]
	return x
'''

n = int(input())
for k in range(0, n):
	toSort = []
	maxi = 0
	m = int(input())
	for j in range(0, m):
		line = input().strip().split()
		c = line[1].split("-")[::-1]
		j = 0
		while j < len(c):
			if c[j] == "upper":
				c[j] = "lower"
			elif c[j] == "lower":
				c[j] = "upper"
			j += 1
		if len(c) > maxi:
			maxi = len(c)
		toSort.append([c, line[0][:-1]])
	for c in toSort:
		c[0]+= ["middle"]*(maxi-len(c[0])) + [c[1]]

	toSort = sorted(toSort)
	for p in toSort:
		print(p[1])
	print("="*30)