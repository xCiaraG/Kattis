n, k = [int(x) for x in input().split()]
throws = []
commands = input().split()
i = 0
while i < len(commands):
	if commands[i] == "undo":
		throws = throws[:-int(commands[i+1])]
		i += 2
	else:
		throws.append(int(commands[i]))
		i += 1
print(sum(throws) % n)