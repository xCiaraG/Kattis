def is_palindrome(s):
	return s == s[::-1]

n = int(input())
for _ in range(n):
	i = 0
	num = int(input())
	while not (is_palindrome(str(num - i)) and len(str(num - i)) == 6) and not (is_palindrome(str(num + i)) and len(str(num + i)) == 6):
		i += 1
		
	if (is_palindrome(str(num - i)) and len(str(num - i)) == 6):
		print(num - i)
	else:
		print(num + i)
