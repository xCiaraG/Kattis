numbers = list(map(int, input().strip().split()))
n = (numbers[1] - numbers[0])*numbers[2]
m = numbers[4]
i = 1
while i * m <= n:
	i += 1
print(i+numbers[3])