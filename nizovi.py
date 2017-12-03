def print_current(current, indentation):
	if current:
		print(indentation + current)
		current = ""

line = input().strip()
indentation = ""
current = ""
for i in range(len(line)):
	letter = line[i]
	if letter == "{":
		print_current(current, indentation)
		print(indentation + "{")
		current = ""
		indentation += "  "
	elif letter == "}":
		print_current(current, indentation)
		current = ""
		indentation = indentation[:-2]
		if i + 1 < len(line) and line[i+1] == ",":
			current = "}"
		else:
			print(indentation + "}")
	elif letter == ",":
		print(indentation + current + ",")
		current = ""
	else:
		current += letter

print_current(current, indentation)