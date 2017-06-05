word = input().strip()
if len(word) > 1 and word[:2] == "LX" and (not word.startswith("LXX") or word == "LXXI"):
	word = "XL" + word[2:]
if len(word) == 1 or word[-2:] == "II" or (len(word) > 2 and word[-3:] == "III"):
	print(word)
elif word[-1] == "I" and word[-2] != "L":
	print(word[:-2] + "I" + word[-2])
else: 
	print(word)