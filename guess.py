lowest = 1
highest = 1001
guess = highest//2
print(guess)
line = input().strip()
while line != "correct":
	if line == "lower":
		highest = guess
	else:
		lowest = guess
	guess = (lowest + highest) // 2
	print(guess)
	line = input().strip()