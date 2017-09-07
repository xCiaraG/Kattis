from sys import stdin

def find_degree(line):
	num = len(line)
	n = num - 1
	while n != 0:
		i = 0
		a = True
		while i + n <= num:
			tmp = line[i:n+i]
			if line.find(tmp) == i and tmp not in line[i+1:]:
				a = False
				i = num
			i += 1
		if a:
			return n
		n -= 1

	return 0

lines = stdin.readlines()
for line in lines:
	line = line.strip()
	print(find_degree(line))