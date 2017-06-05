n = int(input())
total = 0
line = list(map(int, input().strip().split()))
line = sorted(line)
line = line[::-1]
i = 0
while i + 2 < len(line):
	total += line[i+2]
	i += 3
print(total)