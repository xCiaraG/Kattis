def can_input(n):
	n = str(n)
	keys = {"1" : "1234567890",
			"2" : "2356890",
			"3" : "369",
			"4" : "4567890",
			"5" : "56890",
			"6" : "69",
			"7" : "7890",
			"8" : "890",
			"9" : "9",
			"0" : "0"}
	a = True
	i = 0
	while i < len(n) - 1:
		a = a and n[i+1] in keys[n[i]]
		i += 1
	return a

n = int(input())
for i in range(0, n):
	m = int(input())
	i = 0
	while not can_input(m+i) and not can_input(m-i):
		i += 1
	if can_input(m+i):
		print(m+i)
	else:
		print(m-i)
