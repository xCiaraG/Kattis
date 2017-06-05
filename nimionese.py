d = {"a": "b", "e": "d", "f": "g", "h": "g", "i": "g", "j": "k", "l": "k", "m": "n",
	 "o": "n", "q": "p", "r": "p", "s": "t", "u": "t", "v": "t", "w": "t", "x": "t",
	 "y": "t", "z": "t"}
ending = {"b": "ah", "c": "ah", "d": "ah", "g": "ah", "k": "oh", "n": "oh", "p": "oh", "t": "uh"}
hard_consonants = "bcdgknpt"
line = input().strip().split()
s = ""
letter = ""
i = 0
while i < len(line):
	tmp = line[i].lower()
	word = tmp.split("-")
	w = ""
	j = 0
	while j < len(word):
		if j == 0 and word[j][0] not in hard_consonants:
			letter = d[word[j][0]]
			w += letter + word[j][1:]
		elif j == 0 and word[j][0] in hard_consonants:
			letter = word[j][0]
			w += word[j]
		else:
			for l in word[j]:
				if l in hard_consonants:
					w += letter
				else:
					w += l
		j += 1
	if w[-1] in hard_consonants:
		w += ending[w[-1]]
	s += w + " "
	i += 1

s = s[0].upper() + s[1:].strip()
print(s)


