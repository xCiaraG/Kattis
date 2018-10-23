number_map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
	 'A': 10, 'B': 8, 'C': 11, 'D': 12, 'E': 13, 'F': 14, 'G': 11, 'H': 15, 'I': 1,
	 'J': 16, 'K': 17, 'L': 18, 'M': 19, 'N': 20, 'O': 0, 'P': 21, 'Q': 0, 'R': 22,
	 'S': 5, 'T': 23, 'U': 24, 'V': 24, 'W': 25, 'X': 26, 'Y': 24, 'Z': 2 }
numbers = [2, 4, 5, 7, 8, 10, 11, 13]

n = int(input())
for _ in range(n):
	m, digits = [x for x in input().split()]
	total = 0
	for i in range(1, 9): 
		total += (numbers[i - 1] * number_map[digits[i - 1]])
	if total % 27 == number_map[digits[-1]]:
		decimal_total = 0
		digits = digits[::-1]
		for i in range(1, 9):
			decimal_total += number_map[digits[i]] * 27**(i-1)
		print("{} {}".format(m, decimal_total))
	else:
		print("{} Invalid".format(m))