def make_maze(line):
	direction, x, y, maze = "east", 0, 0, [["."]]
	for d in line:
		if d == "R":
			direction = right[direction]
		elif d == "B":
			direction = reverse[direction]
		elif d == "L":
			direction = right[reverse[direction]]

		if direction == "east":
			y += 1
		elif direction == "west":
			y -= 1
		elif direction == "north":
			x -= 1
		else:
			x += 1

		if x == -1:
			x = 0
			maze = [["#"]*len(maze[0])] + maze
		elif x >= len(maze):
			maze.append(["#"]*len(maze[0]))
		elif y == -1:
			y = 0
			i = 0
			while i  < len(maze):
				maze[i] = ["#"] + maze[i]
				i += 1
		elif y >= len(maze[0]):
			i = 0
			while i < len(maze):
				maze[i].append("#")
				i += 1
		maze[x][y] = "."
	return maze


right = {"east":"south", "south":"west", "west":"north", "north":"east"}	
reverse = {"north":"south", "south":"north", "east":"west", "west":"east"}	
n = int(input())
print(n)
for i in range(0, n):
	line = input().strip()
	maze = make_maze(line)
	print("{} {}".format(len(maze)+2, len(maze[0]) + 1))
	print("#"*(len(maze[0])+1))
	for p in maze:
		p.append("#")
		print("".join(p))
	print("#"*(len(maze[0])))