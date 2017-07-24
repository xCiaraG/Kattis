import sys
lines = sys.stdin.readlines()
d = {}
for line in lines:
	line = line.strip().split()
	if line[0] == "clear":
		d = {}
	elif line[0] == "def":
		d[line[1]] = int(line[2])
	elif line[0] == "calc":
		total = 0 
		a = True
		if line[1] in d:
			total += d[line[1]]
		else: 
			a = False
		i = 2
		while i < len(line) - 2:
			if line[i] == "+" and line[i+1] in d:
				total += d[line[i+1]]
			elif line[i] == "-" and line[i+1] in d:
				total -= d[line[i+1]]
			else:
				a = False
			i += 2
		for key in d:
			if d[key] == total:
				total = key
		if a and type(total) == str:
			print(" ".join(line[1:]), total)
		else:
			print(" ".join(line[1:]), "unknown")