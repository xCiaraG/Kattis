def convert(n):
	tmp1 = str(bin(n))[2:]
	if len(tmp1) != 8:
		tmp1 = "0"*(4 - len(tmp1) % 4) + tmp1
	tmp2 = tmp1[1:] + "0"
	ans = ""
	i = 0
	while i < len(tmp1):
		if (tmp1[i] == "0" and tmp2[i] == "1") or (tmp1[i] == "1" and tmp2[i] == "0"):
			ans += "1"
		else:
			ans += "0"
		i += 1
	return int(ans, 2)

n = input()
d = {}
for i in range(0, 256):
	d[convert(i)] = i
print(*[d[int(x)] for x in input().split()])
