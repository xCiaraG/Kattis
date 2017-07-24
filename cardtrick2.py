n = int(input())
for i in range(0,n):
	num = int(input())
	tmp = []
	for j in range(0, num):
		tmp.append([])
	if num == 1:
		tmp[0].append(1)
	else:
		tmp[1].append(1)
	i = 1
	pos = 2
	count = 0
	while pos <= num:
		if i == len(tmp)-1:
			i = 0
		else:
			i += 1
		if count == pos and not tmp[i]:
			tmp[i].append(pos)
			pos += 1
			count = 0
		elif not tmp[i]:
			count += 1
	l = ""
	for c in tmp:
		l += str(c[0]) + " "
	print(l.strip())

