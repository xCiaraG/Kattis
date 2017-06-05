import sys
lines = sys.stdin.readlines()
words = []
m = 0
i = 0
while i < len(lines):
	line = lines[i].strip()
	if line:
		words.append(line[::-1])
		if len(line) > m:
			m = len(line)
	else:
		words = sorted(words)
		for word in words:
			print(" "*(m-len(word))+word[::-1])
		words = []
		m = 0
		if i != len(line) - 1:
			print()
	i += 1
words = sorted(words)
for word in words:
	print(" "*(m-len(word))+word[::-1])