from sys import stdin

words = stdin.readline().strip()
length = len(words) // 3
ans = ""
for i in range(length):
	la = words[i]
	lb = words[i + length]
	lc = words[i + (length * 2)]
	if la == lb:
		ans += la
	elif la == lc:
		ans += la
	else:
		ans += lb
print(ans)