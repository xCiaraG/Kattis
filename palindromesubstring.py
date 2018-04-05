from sys import stdin

lines = stdin.readlines()
for line in lines:
	words = set()
	line = line.strip()
	reverse = line[::-1]
	length = len(line)
	for i in range(2, length+1):
		j = 0
		while i + j < length+1:
			if j != 0 and line[j:i+j] == reverse[-(i + j):-j]:
				words.add(line[j:i+j])
			elif j == 0 and line[:i] == reverse[-i:]:
				words.add(line[:i])
			j += 1
	for w in sorted(list(words)):
		print(w)
	print