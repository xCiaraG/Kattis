line = list(map(float, input().strip().split()))
while line != [0]:
	print(((abs(line[0]-line[2])**line[4]+abs(line[1]-line[3])**line[4])**(1/line[4])))
	line = list(map(float, input().strip().split()))