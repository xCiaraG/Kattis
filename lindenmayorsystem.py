n, m = [int(x) for x in input().split()]
d = {}
for i in range(n):
	line = input().split()
	d[line[0]] = line[-1]
new = input().strip()
for i in range(m):
	to_convert = new
	new = ""
	for letter in to_convert:
		if letter in d:
			new += d[letter]
		else:
			new += letter
print(new)