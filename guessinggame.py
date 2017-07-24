import sys
lines = sys.stdin.readlines()
i = 0
while i + 2 < len(lines):
	low, high = 1, 10
	n = int(lines[i].strip())
	result = lines[i+1].strip()
	a = True
	while result != "right on":
		if result == "too high":
			if n <= low:
				a = False
			if n - 1 < high:
				high = n - 1
		if result == "too low":
			if n >= high:
				a = False
			if n + 1 > low:
				low = n + 1
		i += 2
		n = int(lines[i].strip())
		result = lines[i+1].strip()
	if n < low or n > high or not a:
		print("Stan is dishonest")
	else:
		print("Stan may be honest")
	i += 2
