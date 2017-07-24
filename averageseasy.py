n = int(input())
for i in range(0, n):
	x = input()
	count = 0
	computer_economics = list(map(int, input().strip().split()))
	computer = list(map(int, input().strip().split()))
	economics =  list(map(int, input().strip().split()))
	total_computer = sum(computer)
	total_economics = sum(economics)
	average_computer = total_computer/computer_economics[0]
	average_econmoics = total_economics/computer_economics[1]
	for person in computer:
		if (total_computer - person)/(computer_economics[0] - 1) > average_computer and (total_economics + person)/(computer_economics[1] + 1) > average_econmoics:
			count += 1
	print(count) 