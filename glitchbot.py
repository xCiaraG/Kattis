def determine_location(directions):
	x, y = 0, 0
	position = 0
	for direction in directions:
		if direction == "Right":
			position += 1
			position = position % 4
		elif direction == "Left":
			position += 3
			position = position % 4
		elif position == 0:
			y += 1
		elif position == 1:
			x += 1
		elif position == 2:
			y -= 1
		else:
			x -= 1
	return x, y

x, y = [int(x) for x in input().split()]
n = int(input())
directions = []
for i in range(n):
	directions.append(input().strip())

i = 0
while (x, y) != determine_location(directions[:i] + ["Forward"] + directions[i+1:]) and (x, y) != determine_location(directions[:i] + ["Right"] + directions[i+1:]) and (x, y) != determine_location(directions[:i] + ["Left"] + directions[i+1:]):
	i += 1

if (x, y) == determine_location(directions[:i] + ["Forward"] + directions[i+1:]):
	print(i+1, "Forward")
elif (x, y) == determine_location(directions[:i] + ["Right"] + directions[i+1:]):
	print(i+1, "Right")
else:
	print(i+1, "Left")