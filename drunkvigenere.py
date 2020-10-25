from sys import stdin

c = stdin.readline().strip()
k = stdin.readline().strip()

res = ""

for i in range(len(c)):
	l = ord(c[i]) - 65
	if i % 2 == 0:
		l -= (ord(k[i]) - 65)
	else:
		l += (ord(k[i]) - 65)
	l %= 26
	res += chr(l + 65)
print(res)
