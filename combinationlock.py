line = list(map(int, input().strip().split()))
while line != [0, 0, 0, 0]:
	t = 1080
	t += ((abs(line[0] - line[1] + 40)% 40) * 9)
	t += ((abs(line[2] - line[1] + 40)% 40) * 9)
	t += ((abs(line[2] - line[3] + 40)% 40) * 9)
	print(t) 
	line = list(map(int, input().strip().split()))
