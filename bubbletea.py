n = int(input())
teas = [int(x) for x in input().split()]
_ = input()
toppings = [int(x) for x in input().split()]
minimum = 2000
for i in range(n):
	for j in [int(x) for x in input().split()][1:]:
		if teas[i] + toppings[j-1] < minimum:
			minimum = teas[i] + toppings[j-1]
money = int(input())
if (money//minimum) - 1 >= 0:
	print((money//minimum) - 1)
else:
	print(0)