from sys import stdin
def add_to_tree(n, p):
	while p <= n_bits:
		sum_bits[p] += n
		p += int(p & -p)

def find_sum(p):
	t = 0
	while p != 0:
		t += sum_bits[p]
		p -= int(p & -p)
	return t

line = [int(x) for x in input().split()]
n_bits = line[0]
n = line[1]
bits = [0]*(n_bits+1)
sum_bits = [0]*(n_bits+1)
for _ in range(0, n):
	line = input().split()
	if line[0] == "F":
		m = int(line[1])
		tmp = int(not bits[m])
		bits[m] = tmp
		if not tmp:
			tmp = -1
		add_to_tree(tmp, m)
	else:
		a = find_sum(int(line[1])-1)
		b = find_sum(int(line[2]))
		print(b-a)


    