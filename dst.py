n = int(input())
for i in range(0, n):
	line = input().strip().split()
	minutes = int(line[2])*60 + int(line[3])
	if line[0] == "B":
		minutes -= int(line[1])
	else:
		minutes += int(line[1])

	if minutes < 0:
		minutes += 1440
	elif minutes >= 1440:
		minutes -= 1440

	hours = minutes // 60
	minutes = minutes % 60

	print(hours, minutes)