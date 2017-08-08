from sys import stdin
n = int(stdin.readline())
stack = [0]*2000
for i in range(0, n):
	m = int(stdin.readline())
	t = frozenset()
	c = 0
	for j in range(0, m):
		line = stdin.readline().strip()
		if line == "PUSH":
			stack[c] = t
			c += 1
			print(0)
		elif line == "DUP":
			stack[c] = stack[c-1]
			print(len(stack[c]))
			c += 1
		elif line == "ADD":
			tmp = set(stack[c-2])
			tmp.add(hash(stack[c-1]))
			stack[c-2] = frozenset(tmp)
			c -= 1
			print(len(stack[c-1]))
		elif line == "UNION":
			stack[c-2] = stack[c-2].union(stack[c-1])
			c -= 1
			print(len(stack[c-1]))
		else:
			stack[c-2] = stack[c-2].intersection(stack[c-1])
			c -= 1
			print(len(stack[c-1]))
	print("***")
