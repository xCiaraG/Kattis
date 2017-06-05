line = input().strip()
i = 1
while line != "END":
	line = line.split("*")
	if len(line) > 2:
		line = line[1:-1]
	if len(set(line)) == 1:
		print("{} EVEN".format(i))
	else:
		print("{} NOT EVEN".format(i))
	i += 1
	line = input().strip()
