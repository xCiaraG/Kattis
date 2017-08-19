n = int(input())
while n != 0:
	t = 0
	a = True
	for i in range(0, n):
		line = input().split()
		s = ""
		pos = line[0]
		line = list(map(int, line[1:]))
		if not t:
			t = sum(line)
		elif t != sum(line):
			a = False
		for p in line:
			s += pos*p
			if pos == "#":
				pos = "."
			else:
				pos = "#"
		print(s)
	if not a:
		print("Error decoding image")
	n = int(input())
	if n:
		print()
