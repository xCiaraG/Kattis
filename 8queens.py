r, c, d1, d2 = [], [], [], []
for i in range(0, 8):
	line = input().strip()
	for j in range(0, 8):
		if line[j] == "*":
			r.append(i)
			c.append(j)
			d1.append(i+j)
			d2.append(i-j)

if len(set(r)) == 8 and len(set(c)) == 8 and len(set(d1)) == 8 and len(set(d2)) == 8:
	print("valid")
else:
	print("invalid")