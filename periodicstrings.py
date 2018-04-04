def kperiodic(k, s):
	if len(s) % k != 0:
		return False
	current = s[:k]
	for i in range(0, len(s), k):
		if s[i:i+k] != current:
			return False
		current = current[-1] + current[:-1]
	return True

s = input().strip()
for i in range(1, len(s) + 1):
	if kperiodic(i, s):
		print(i)
		break