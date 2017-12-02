emma = set([int(x) for x in input().split()][1:])
marcos = set([int(x) for x in input().split()][1:])
e, m, t = 0, 0, 0
for i in range(1000000):
	if i in emma and i in marcos:
		t += 1
		e, m = 0, 0
	elif i in emma and m == 0:
		t += 1
		m += 1
		e = 0
	elif i in marcos and e == 0:
		t += 1
		e += 1
		m = 0
print(t)