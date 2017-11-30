def piece1(total):
	for i in range(c - 3):
		if columns[i] == columns[i+1] == columns[i+2] == columns[i+3]:
			total += 1
	return total

def piece2(total):
	for i in range(c - 1):
		if columns[i] == columns[i+1]:
			total += 1
	return total

def piece3(total):
	for i in range(c - 2):
		if columns[i] == columns[i+1] == columns[i+2] - 1:
			total += 1
	for i in range(c - 1):
		if columns[i] - 1 == columns[i+1]:
			total += 1
	return total

def piece4(total):
	for i in range(c - 2):
		if columns[i] - 1 == columns[i+1] == columns[i+2]:
			total += 1
	for i in range(c - 1):
		if columns[i] == columns[i+1] - 1: 
			total += 1
	return total

def piece5(total):
	for i in range(c - 2):
		if columns[i] == columns[i+1] == columns[i+2]:
			total += 1
		if columns[i] - 1 == columns[i+1] == columns[i+2] - 1:
			total += 1
	for i in range(c - 1):
		if columns[i] == columns[i+1] - 1:
			total += 1
		if columns[i] - 1 == columns[i+1]:
			total += 1
	return total

def piece6(total):
	for i in range(c - 2):
		if columns[i] == columns[i+1] == columns[i+2]:
			total += 1
		if columns[i] == columns[i+1] - 1 == columns[i+2] - 1:
			total += 1
	for i in range(c - 1):
		if columns[i] == columns[i+1]:
			total += 1
		if columns[i] - 2 == columns[i+1]:
			total += 1
	return total

def piece7(total):
	for i in range(c - 2):
		if columns[i] == columns[i+1] == columns[i+2]:
			total += 1
		if columns[i] - 1 == columns[i+1] - 1 == columns[i+2]:
			total += 1
	for i in range(c - 1):
		if columns[i] == columns[i+1]:
			total += 1
		if columns[i] == columns[i+1] - 2:
			total += 1
	return total

c, p = [int(x) for x in input().split()]
columns = [int(x) for x in input().split()]

if p == 1:
	print(piece1(c))
elif p == 2:
	print(piece2(0))
elif p == 3:
	print(piece3(0))
elif p == 4:
	print(piece4(0))
elif p == 5:
	print(piece5(0))
elif p == 6:
	print(piece6(0))
else:
	print(piece7(0))