line = list(map(int, input().strip().split()))
while line != [0, 0]:
	robot_think_x, robot_think_y, actually_x, actually_y = 0, 0, 0, 0
	w = line[0]
	l = line[1]
	n = int(input())
	for i in range(0, n):
		tmp = input().strip().split()
		if tmp[0] == "u":
			robot_think_y += int(tmp[1])
			actually_y += int(tmp[1])
		elif tmp[0] == "d":
			robot_think_y -= int(tmp[1])
			actually_y -= int(tmp[1])
		elif tmp[0] == "r":
			robot_think_x += int(tmp[1])
			actually_x += int(tmp[1])
		elif tmp[0] == "l":
			robot_think_x -= int(tmp[1])
			actually_x -= int(tmp[1])
		if actually_x >= w:
			actually_x = w-1
		elif actually_x < 0:
			actually_x = 0
		elif actually_y >= l:
			actually_y = l-1
		elif actually_y < 0:
			actually_y = 0
	print("Robot thinks {} {}".format(robot_think_x, robot_think_y))
	print("Actually at {} {}".format(actually_x, actually_y))
	print()
	line = list(map(int, input().strip().split()))
