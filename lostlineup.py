from sys import stdin
n = int(stdin.readline())
line = [int(x) for x in stdin.readline().split()]
res = ["1"]
for i in range(n-1):
	res.append(str(line.index(i)+2))
print(" ".join(res))