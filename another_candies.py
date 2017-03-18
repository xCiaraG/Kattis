import sys
n = int(sys.stdin.readline().strip())
for i in range(0,n):
	line = sys.stdin.readline()
	m = int(sys.stdin.readline().strip())
	total = 0
	for j in range(0,m):
		total += int(sys.stdin.readline().strip())
	if total% m == 0:
		print("YES")
	else:
		print("NO")