def multigram(sentence, part, l):
	part = sorted(list(part))
	for i in range(0, len(sentence), l):
		if sorted(list(sentence[i:i+l])) != part:
			return False
	return True

word = input().strip()
root = -1
for i in range(1, (len(word)//2) + 1):
	if len(word) % i == 0 and multigram(word[i:], word[:i], i):
		root = word[:i]
		break
print(root)
