n = int(input())
while n != 0:
	current = ["?" for i in range(32)]
	for i in range(n):
		cmd = input().split()
		if cmd[0] == "CLEAR":
			current[int(cmd[1])] = False
		elif cmd[0] == "SET":
			current[int(cmd[1])] = True
		elif cmd[0] == "AND":
			tmp1, tmp2 = current[int(cmd[1])], current[int(cmd[2])]
			if type(tmp1) == bool and type(tmp2) == bool:
				current[int(cmd[1])] = tmp1 and tmp2
			elif not tmp2 or not tmp1:
				current[int(cmd[1])] = False
			else:
				current[int(cmd[1])] = "?"
		else:
			tmp1, tmp2 = current[int(cmd[1])], current[int(cmd[2])]
			if type(tmp1) == bool and type(tmp2) == bool:
				current[int(cmd[1])] = tmp1 or tmp2
			elif type(tmp2) == bool and tmp2:
				current[int(cmd[1])] = True
			elif not tmp1:
				current[int(cmd[1])] = "?"
	print("".join(["1" if x == True else "0" if not x else x for x in current])[::-1])
	n = int(input())
