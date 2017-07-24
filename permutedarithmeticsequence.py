def sequence(l):
	diff = l[0] - l[1]
	i = 0
	while i + 1 < len(l):
		if diff != l[i] - l[i+1]:
			return False
		i += 1
	return True


n = int(input())
for i in range(0, n):
	line = list(map(int, input().strip().split()))
	line = line[1:]
	if sequence(line):
		print("arithmetic")
	elif sequence(sorted(line)):
		print("permuted arithmetic")
	else:
		print("non-arithmetic")
