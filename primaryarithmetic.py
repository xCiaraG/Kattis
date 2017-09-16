from sys import stdin
lines = stdin.readlines()
for line in lines[:-1]:
	x1, x2 = line.split()
	t, carry, i, j = 0, 0, len(x1)-1, len(x2)-1
	while i >= 0 or j >= 0:
		tmp = carry
		if i >= 0:
			tmp += int(x1[i]) 
		if j >= 0:
			tmp += int(x2[j]) 

		if tmp > 9:
			t += 1
			carry = 1
		else:
			carry = 0
		i -= 1
		j -= 1

	if t == 0:
		print("No carry operation.")
	elif t == 1:
		print("1 carry operation.")
	else:
		print("{} carry operations.".format(t))

