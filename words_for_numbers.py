import sys
single = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
		  7: "seven", 8: "eight", 9: "nine"}
teens = {11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
		 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
		 19: "nineteen"}
tens = {1: "ten", 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty",
		7: "seventy", 8: "eighty", 9: "ninety"}

lines = sys.stdin.readlines()
for line in lines:
	line = line.split()
	s = ""
	i = 0
	for word in line:
		if (len(word) == 1 and word[0] in "0123456789") or (len(word) == 2 and word[0] in "0123456789" and word[1] in "0123456789"):
			if len(word) == 1:
				tmp = single[int(word[0])] + " "
			elif word[1] == "0":
				tmp = tens[int(word[0])] + " "
			elif word[0] == "1":
				tmp = teens[int(word)] + " "
			else:
				tmp = tens[int(word[0])] + "-" + single[int(word[1])] + " "
			if not s:
				s += tmp[0].upper() + tmp[1:]
			else:
				s += tmp
		else: 
			s += word + " "  
	print(s.strip())
