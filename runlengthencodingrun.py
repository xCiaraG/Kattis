def encode(s):
	new = ''
	prev = s[0]
	count = 1
	for i in range(1, len(s)):
		if s[i] == prev:
			count += 1
		else:
			new += prev + str(count)
			prev = s[i] 
			count = 1
	new += prev + str(count)
	return new

def decode(s):
	new = ''
	for i in range(0, len(s), 2):
		new += s[i] * int(s[i+1])
	return new

e_d, s = input().strip().split()
if e_d == 'E':
	print(encode(s))
else:
	print(decode(s))