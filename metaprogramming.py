import sys
d = {}
lines = sys.stdin.readlines()
for line in lines:
	line = line.strip().split()
	if line[0] == "define":
		d[line[2]] = int(line[1])
	elif line[1] not in d or line[3] not in d:
		print("undefined")
	elif line[2] == "=":
		if d[line[1]] == d[line[3]]:
			print("true")
		else:
			print("false")
	elif line[2] == "<":
		if d[line[1]] < d[line[3]]:
			print("true")
		else:
			print("false")
	else:
		if d[line[1]] > d[line[3]]:
			print("true")
		else:
			print("false")

