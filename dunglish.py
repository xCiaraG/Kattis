n = input()
sentence = input().split()
m = int(input())
d = {}
for i in range(m):
	words = input().split()
	if words[0] not in d:
		d[words[0]] = [[0, 0], ""]
	if words[2] == "correct":
		d[words[0]][0][0] += 1
		d[words[0]][1] = words[1]
	else:
		d[words[0]][0][1] += 1
		d[words[0]][1] = words[1]

correct = 1
total = 1
for word in sentence:
	correct *= d[word][0][0]
	total *= sum(d[word][0])

if correct == 1 or total == 1:
	s = ""
	for word in sentence:
		s += d[word][1] + " "
	print(s.strip())
	if correct == 1:
		print("correct")
	else:
		print("incorrect")
else:
	print("{} correct".format(correct))
	print("{} incorrect".format(total - correct))



