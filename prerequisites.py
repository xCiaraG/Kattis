from sys import stdin
lines = stdin.readlines()
i = 0
while i < len(lines) - 1:
	k, m = [int(x) for x in lines[i].split()]
	courses = set([x for x in lines[i+1].split()])
	i += 2
	ans = True
	for j in range(m):
		category = [x for x in lines[i+j].split()]
		if len(courses.intersection(set(category[2:]))) < int(category[1]):
			ans = False
	i += m
	if ans:
		print("yes")
	else:
		print("no")
