n = int(input())
for i in range(0, n):
	s = ""
	m = []
	message = input().strip()
	square = int(len(message)**0.5)
	i = 0
	while i < len(message):
		m.append(message[i:i+square])
		i += square
	j = square-1
	while j >= 0:
		i = 0
		while i < len(m):
			s += m[i][j]
			i += 1
		j -= 1
	print(s)

