line = [int(x) for x in input().split()]
while line != [0, 0]:
	n1 = line[0]
	n2 = line[1]
	n1_pattern = [n1]
	n2_pattern = [n2]
	if n1 == n2:
		print("{0} needs 0 steps, {0} needs 0 steps, they meet at {0}".format(n1))
	else:
		while n1 != 1 or n2 != 1:
			if n1 != 1:
				if n1 % 2 == 0:
					n1 = n1 // 2
				else:
					n1 = (3*n1) + 1
				n1_pattern.append(n1)
				if n1 in n2_pattern:
					print("{} needs {} steps, {} needs {} steps, they meet at {}".format(n1_pattern[0], len(n1_pattern)-1, n2_pattern[0], n2_pattern.index(n1), n1))
					n1, n2, = 1, 1
			if n2 != 1:
				if n2 % 2 == 0:
					n2 = n2 // 2
				else:
					n2 = (3*n2) + 1
				n2_pattern.append(n2)
				if n2 in n1_pattern:
					print("{} needs {} steps, {} needs {} steps, they meet at {}".format(n1_pattern[0], n1_pattern.index(n2), n2_pattern[0], len(n2_pattern)-1, n2))
					n1, n2, = 1, 1
	line = [int(x) for x in input().split()]


