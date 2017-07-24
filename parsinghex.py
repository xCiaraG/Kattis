import sys
lines = sys.stdin.readlines()
for line in lines:
	i = 0
	while i < len(line) + 1:
		if line[i:i+2] == "0x" or line[i:i+2] == "0X":
			tmp = i + 2
			while tmp < len(line) and line[tmp] in "0123456789ABCDEFabcdef":
				tmp += 1
			n = int(line[i+2:tmp], 16)
			print(line[i:tmp], n)
			i = tmp - 1
		i += 1

