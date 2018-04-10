year = int(input())

if (((year - 2018) * 12) + 8) % 26 < 12:
	print("yes")
else:
	print("no")