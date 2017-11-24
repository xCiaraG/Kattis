def calculate(line, tmp):
	line = line.split(tmp)
	return len(line) - 1 + len("".join(line))

line = input().strip()
m = len(line)
for i in range(len(line)):
	for j in range(i+2, len(line)):
		tmp = line[i:j]
		total = j - i
		total += calculate(line, tmp)
		if total < m:
			m = total
print(m)
