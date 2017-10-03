from sys import stdin
r, c = [int(x) for x in stdin.readline().split()]
columns = [""]*c
for _ in range(r):
	line = stdin.readline().strip()
	for i in range(c):
		columns[i] += line[i]

for i in range(c):
	s = columns[i].split("#")
	for j in range(len(s)):
		tmp = s[j].count(".")
		s[j] = "."*tmp + "a"*(len(s[j])-tmp)
	columns[i] = "#".join(s)

for i in range(r):
	tmp = ""
	for j in range(c):
		tmp += columns[j][i]
	print(tmp)