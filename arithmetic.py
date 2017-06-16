'''
num = int(input().strip())
num = int(str(num), 8)
s = str(hex(num))[2:]
a = ""
for l in s:
    if l in "abcdef":
        a += l.upper()
    else:
        a += l
print(a)
'''
oct_to_bin = {"0" : "000", "1": "001", "2": "010", 
			  "3" : "011", "4": "100", "5": "101", 
			  "6" : "110", "7": "111"}

bin_to_hex = {"0000" : "0", "0001": "1", "0010": "2",
			  "0011" : "3", "0100": "4", "0101": "5",
			  "0110" : "6", "0111": "7", "1000": "8",
			  "1001" : "9", "1010": "A", "1011": "B",
			  "1100" : "C", "1101": "D", "1110": "E",
			  "1111" : "F"}

n = input().strip()
newn = ""
length = len(n)
i = 0
while i < length:
	newn += oct_to_bin[n[i]]
	i += 1

while len(newn) % 4 != 0:
	newn = "0" + newn

n = ""
length = len(newn)
i = 0
while i + 3 < length:
	n += bin_to_hex[newn[i:i+4]]
	i += 4

while n[0] == "0" and len(n) != 1:
	n = n[1:]

print(n)