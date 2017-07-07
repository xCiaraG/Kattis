n = input()
line = list(map(int, input().strip().split()))
s = sum(line)
m = max(line)
if s/m >= 2:
	print(s)
else:
	print(m*2)