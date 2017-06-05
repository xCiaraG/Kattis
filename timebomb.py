import sys
numbers = {"**** ** ** ****": "0", "  *  *  *  *  *": "1", "***  *****  ***": "2", "***  ****  ****":"3",
			"* ** ****  *  *": "4", "****  ***  ****": "5", "****  **** ****": "6", 
			"***  *  *  *  *": "7", "**** ***** ****": "8", "**** ****  ****": "9"}
d1, d2, d3, d4, d5, d6, d7, d8 = "", "", "", "", "", "", "", ""
lines = sys.stdin.readlines()
for line in lines:
	i = 0
	while i < len(line) - 2:
		if i == 0:
			d1 += line[i:i+3]
		elif i == 4:
			d2 += line[i:i+3]
		elif i == 8:
			d3 += line[i:i+3]
		elif i == 12:
			d4 += line[i:i+3]
		elif i == 16:
			d5 += line[i:i+3]
		elif i == 20:
			d6 += line[i:i+3]
		elif i == 24:
			d7 += line[i:i+3]
		elif i == 28:
			d8 += line[i:i+3]
		i += 4

n = ""
tmp = [d1, d2, d3, d4, d5, d6, d7, d8]
a = True
for digit in tmp:
	if digit:
		if digit in numbers:
			n += numbers[digit]
		else:
			a = False
n = int(n)
if n % 6 == 0 and a:
	print("BEER!!")
else:
	print("BOOM!!")

