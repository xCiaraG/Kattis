import sys
lines = sys.stdin.readlines()
i = 0
case = 1
while i < len(lines):
	n = int(lines[i].strip())
	to_test = []
	for j in range(0, n):
		i += 1
		to_test.append(int(lines[i].strip()))
	to_test = sorted(to_test)
	i += 1
	m = int(lines[i].strip())
	print("Case {}:".format(case))
	case += 1
	for k in range(0, m):
		i += 1
		a = 0
		b = len(to_test) - 1
		test = int(lines[i].strip())
		diff = abs(test - (to_test[a] + to_test[b]))
		s = to_test[a] + to_test[b]
		while a < b:
			if abs(test - (to_test[a] + to_test[b])) < diff:
				diff = abs(test - (to_test[a] + to_test[b]))
				s = to_test[a] + to_test[b]
			if to_test[a] + to_test[b] > test:
				b -= 1
			else:
				a += 1
		print("Closest sum to {} is {}.".format(test, s))
	i += 1
