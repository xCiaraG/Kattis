def find_pattern(s):
	for i in range(1, len(s) + 1):
		if (s[:i] * ((len(s) // i) + 1))[:len(s)] == s:
			return i

n = int(input())
for _ in range(n):
	print(find_pattern(input()))