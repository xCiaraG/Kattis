import math
def find_hash(s):
	if s:
		l1 = int(bin(ord(s[0])), 2)
	for l2 in s[1:]:
		l1 = int(l1 ^ int(bin(ord(l2)), 2))
	return l1

n = int(input())
while n != 0:
	d = {}
	collisions = 0
	for i in range(0, n):
		s = input()
		h = find_hash(s)
		if h not in d:
			d[h] = [s, 1]
		elif s not in d[h]:
			d[h].append(s)
			d[h].append(1)
		else:
			d[h][d[h].index(s)+1] += 1
	unique = 0 
	for k in d:
		unique += len(d[k]) // 2
		if len(d[k]) > 2:
			tmp = d[k]
			i = 0 
			while i < len(tmp) - 1:
				j = i + 2
				while j < len(tmp) - 1:
					collisions += tmp[i+1] * tmp[j+1]
					j += 2
				i += 2
	print("{} {}".format(unique, collisions))
	n = int(input())

