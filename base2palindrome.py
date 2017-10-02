from sys import stdin
n = int(stdin.readline().strip())
a = n
i = 0
odd = False
s = "1"
while n != 1:
	if "0" not in s:
		if odd:
			i += 1
		odd = not odd
		s = "1" + "0"*i
	elif s[-1] == "0":
		s = s[:-1] + "1"
	else:
		tmp = s[::-1].index("0")
		s = s[:-tmp-1] + "1" + "0"*tmp
	n -= 1

if a == 1:
	print(1)
elif odd:
	print(int(s + s[::-1], 2))
else:
	print(int(s[:-1] + s[::-1], 2))