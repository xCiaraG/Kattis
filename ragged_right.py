import sys
lines = sys.stdin.readlines()
m = 0
for line in lines:
	line = line.strip()
	if len(line) > m:
		m = len(line)
total = 0
for line in lines[:-1]:
	line = line.strip()
	total += (m-len(line))**2

print(total)


