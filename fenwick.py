from sys import stdin
def add_to_tree(n, p):
	while p <= length:
		numbers[p] += n
		p += int(p & -p)

def find_sum(p):
	t = 0
	while p != 0:
		t += numbers[p]
		p -= int(p & -p)
	return t

line = [int(x) for x in stdin.readline().split()]
length = line[0]+1
numbers = [0]*(length+2)
n = line[1]
for i in range(0, n):
	line = stdin.readline().split()
	if line[0] == "?":
		if int(line[1]) != 0:
			print(find_sum(int(line[1])))
		else:
			print(0)
	else:
		add_to_tree(int(line[2]), int(line[1])+1)
