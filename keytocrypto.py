alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sentence = input().strip()
key = input().strip()
s = ""
i = 0
for letter in sentence:
	s += alphabet[(alphabet.index(letter) - alphabet.index(key[i])) % 26]
	key += s[-1]
	i += 1
print(s)