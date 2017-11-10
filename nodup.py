line = input().split()
if len(line) == len(set(line)):
	print("yes")
else:
	print("no")