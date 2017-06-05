import sys
lines = sys.stdin.readlines()
d = {}
lines = lines[:-1]
for line in lines:
	line = line.strip().split()
	if len(line) > 1 and line[1] == "=":
		d[line[0]] = int(line[2])
	else:
		new = [0]
		for n in line:
			if n in d:
				new[0] += d[n]
			elif n[0] in "123456789":
				new[0] += int(n)
			elif n != "+":
				new.append(n)
		if new[0] != 0:
			new[0] = str(new[0])
		else:
			new.remove(new[0])
		print(" + ".join(new))

