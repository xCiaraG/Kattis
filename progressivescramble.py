def encrypt(sentence):
	new = ""
	t = 0
	for letter in sentence:
		t += letters.index(letter)
		new += letters[t % 27]
	return new

def decrypt(sentence):
	new = ""
	t = 0
	for letter in sentence:
		tmp = 0
		while letters.index(letter) - t + tmp < 0:
			tmp += 27
		tmp += letters.index(letter) - t
		t += tmp
		new += letters[tmp]
	return new

letters = " abcdefghijklmnopqrstuvwxyz"
n = int(input())
for i in range(n):
	sentence = input()
	if sentence[0] == "e":
		print(encrypt(sentence[2:]))
	else:
		print(decrypt(sentence[2:]))