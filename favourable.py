def calculate(s):
	if s in num_fav:
		return num_fav[s]
	else:
		tmp = d[s]
		total = calculate(tmp[0]) + calculate(tmp[1]) + calculate(tmp[2])
		num_fav[s] = total 
		return total

n = int(input())
for i in range(0, n):
	m = int(input())
	d = {}
	num_fav = {}
	total = 0
	for j in range(0, m):
		line = input().strip().split(" ", 1)
		if line[1] == "favourably":
			num_fav[line[0]] = 1
		elif line[1] == "catastrophically":
			num_fav[line[0]] = 0
		else:
			d[line[0]] = line[1].split()
	calculate("1")
	print(num_fav["1"])