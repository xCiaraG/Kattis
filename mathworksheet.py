n = int(input())
while n != 0:
	answers = []
	for i in range(0, n):
		line = input().strip().split()
		if line[1] == "*":
			answers.append(int(line[0]) * int(line[2]))
		elif line[1] == "+":
			answers.append(int(line[0]) + int(line[2]))
		if line[1] == "-":
			answers.append(int(line[0]) - int(line[2]))
		answers = list(map(str, answers))
	l = len(max(answers, key=len))
	per_line = 51//(l+1)
	tmp_per_line = 1
	j = 0
	while j < len(answers):
		print("{:>{}}".format(answers[j], l), end='')
		if j + 1 == len(answers):
			print()
		elif tmp_per_line == per_line:
			print()
			tmp_per_line = 0
		else:
			print(" ", end='')
		j += 1
		tmp_per_line += 1
	n = int(input())
	if n != 0:
		print()

