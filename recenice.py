def number_to_word(n):
	n = str(n)
	ones = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
			"6": "six", "7": "seven", "8": "eight", "9": "nine"}
	teens = {"11": "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen",
			 "15": "fifteen", "16": "sixteen", "17": "seventeen", "18": "eighteen",
			 "19": "nineteen"}
	tens = {"1": "ten", "2": "twenty", "3": "thirty", "4": "forty", "5": "fifty",
			"6": "sixty", "7": "seventy", "8": "eighty", "9": "ninety"}
	s = ""
	if len(n) == 3:
		s += ones[n[0]] + "hundred"
		n = n[1:]
		if n == "00":
			return s
	if len(n) == 2:
		if n[1] == "0":
			s += tens[n[0]]
			return s
		elif n[0] == "1":
			s += teens[n]
			return s
		elif n[0] == "0":
			s += ones[n[1]]
			return s
		s += tens[n[0]]
	s += ones[n[-1]]
	return s

n = int(input())
s = []
count = 0
for i in range(0, n):
	line = input().strip()
	if line == "$":
		s.append("")
		place = i
	else:
		s.append(line)
		count += len(line)
n = "tmp"
num = count
while count + len(n) != num:
	num += 1
	n = number_to_word(num)
s[place] = n
print(" ".join(s))