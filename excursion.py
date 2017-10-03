line = input().strip()
x, y, z, t = 0, 0, 0, 0
for c in line:
	if c == "0":
		x += 1
		t += y + z
	elif c == "1":
		y += 1
		t += z
	else:
		z += 1
print(t)
