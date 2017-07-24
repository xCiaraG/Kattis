def check_letter(a, b):
	seen = [a]
	to_check = [a]
	tmp = []
	while to_check:
		for letter in to_check:	
			for l in letter_translations[letter]:
				if l not in seen:
					seen.append(l)
					tmp.append(l)
		to_check = tmp
		tmp = []
	if b in seen:
		return True
	else:
		return False

nums = list(map(int, input().strip().split()))
letter_translations = {"a": ["a"],"b": ["b"],"c": ["c"],"d": ["d"],"e": ["e"],"f": ["f"],
					   "g": ["g"],"h": ["h"],"i": ["i"],"j": ["j"],"k": ["k"],"l": ["l"],
					   "m": ["m"],"n": ["n"],"o": ["o"],"p": ["p"],"q": ["q"],"r": ["r"],
					   "s": ["s"],"t": ["t"],"u": ["u"],"v": ["v"],"w": ["w"],"x": ["x"],
					   "y": ["y"],"z": ["z"],}
for i in range(0, nums[0]):
	letters = input().strip().split()
	if letters[1] not in letter_translations[letters[0]]:
		letter_translations[letters[0]].append(letters[1])
for j in range(0, nums[1]):
	words = input().strip().split()
	i = 0
	a = True
	while i < len(words[0]) and i < len(words[1]) and a:
		if not check_letter(words[0][i], words[1][i]):
			a = False 
		i += 1
	if a and len(words[0])==len(words[1]):
		print("yes")
	else:
		print("no")
