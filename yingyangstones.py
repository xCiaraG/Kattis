line = input().strip()
i = 0
B = 0
W = 0
while i < len(line):
	if line[i] == "B":
		B += 1
	else:
		W += 1
	if B+W > 2:
		if W-B == 1:
			if i + 1 < len(line):
				line = "W" + line[i+1:]
				i, B, W = -1, 0, 0
		elif B-W == 1:
			if i + 1 < len(line):
				line = "B" + line[i+1:]
				i, B, W = -1, 0, 0
	i += 1
if line == "BW" or line == "WB":
	print(1)
else:
	print(0)