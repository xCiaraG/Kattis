key = list(map(int, input().strip().split()))[1:]
while key:
	line = input().strip()
	new = ""
	if len(line) % len(key) != 0:
		line += " "*(len(key) - (len(line)% len(key)))
	i = 0
	while i < len(line):
		part = line[i:i+len(key)]
		for j in key:
			new += part[j-1]
		i += len(key)
	print("'" + new + "'")
	key = list(map(int, input().strip().split()))[1:]

