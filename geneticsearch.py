def count_occurances(s1, s2):
	count = 0
	l = len(s1)
	for i in range(len(s2) - l + 1):
		if s1 == s2[i:i+l]:
			count += 1
	return count

line = input().strip()
while line != "0":
	s1, s2 = line.split()
	
	type1, type2, type3 = count_occurances(s1, s2), 0, 0
	
	delete = set()
	for i in range(len(s1)):
		delete.add(s1[:i] + s1[i+1:])
	for s in delete:
		type2 += count_occurances(s, s2)

	add = set()
	for i in range(len(s1) + 1):
		add.add(s1[:i] + "A" + s1[i:])
		add.add(s1[:i] + "G" + s1[i:])
		add.add(s1[:i] + "C" + s1[i:])
		add.add(s1[:i] + "T" + s1[i:])
	for s in add:
		type3 += count_occurances(s, s2)

	print(type1, type2, type3)
	line = input().strip()