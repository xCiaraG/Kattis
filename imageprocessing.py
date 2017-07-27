line = [int(x) for x in input().split()]
matrix, kernel = [], []

for i in range(0, line[0]):
	matrix.append([int(x) for x in input().split()])

for i in range(0, line[2]):
	kernel.append([int(x) for x in input().split()][::-1])

kernel = kernel[::-1]
new = []
i = 0
while i < line[0] - line[2] + 1:
	j = 0
	tmp = []
	while j < line[1] - line[3] + 1:
		t = 0
		n = 0
		while n < line[2]:
			m = 0
			while m < line[3]:
				t += kernel[n][m]*matrix[i+n][j+m]
				m += 1
			n += 1
		tmp.append(t)
		j += 1
	new.append(tmp)
	i += 1
for m in new:
	print(*m)