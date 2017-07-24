s = input().strip()
m = {"R": "S", "B": "K", "L": "H"}
new_s = ""
length = len(s)
i = 0
while i + 2 < length:
	tmp = s[i:i+3]
	if "R" in tmp and "B" in tmp and "L" in tmp:
		new_s += "C"
		i += 2
	else:
		new_s += m[s[i]]
	i += 1

while i < length:
	new_s += m[s[i]]
	i += 1
print(new_s)
