from sys import stdin
lines = stdin.readlines()
for line in lines:
	values = []
	numbers = [int(x) for x in line.split()]
	for i in range(1, numbers[0]):
		values.append(abs(numbers[i]-numbers[i+1]))
	if sorted(values) == [i for i in range(1, numbers[0])]:
		print("Jolly")
	else:
		print("Not jolly")
