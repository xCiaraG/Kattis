line = input().strip().split()
word, guess = list(line[1]), list(line[2])	
i, r, s = 0, 0, 0
while i < len(word):
	if word[i] == guess[i]:
		r += 1
		word.remove(word[i])
		guess.remove(guess[i])
	else:
		i += 1
i = 0
while i < len(word):
	if word[i] in guess:
		s += 1
		guess.remove(word[i])
	i += 1
print(r, s)

