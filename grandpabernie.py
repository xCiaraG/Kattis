n = int(input())
d = {}
for i in range(0, n):
	line = input().strip().split()
	if line[0] not in d:
		d[line[0]] = [int(line[1])]
	else:
		d[line[0]].append(int(line[1]))

for k in d:
	d[k] = sorted(d[k])

n = int(input())
for i in range(0, n):
	line = input().strip().split()
	print(d[line[0]][int(line[1])-1])