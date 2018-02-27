numbers = [i**3 for i in range(1, 74)]
sums = sorted([numbers[i] + j for i in range(len(numbers)) for j in numbers[i + 1:]])
bus_numbers = []
for n in sums:
	if sums.count(n) > 1 and n not in bus_numbers:
		bus_numbers.append(n)
n = int(input())
for i in range(len(bus_numbers) + 1):
	if i < len(bus_numbers) and bus_numbers[i] > n:
		break

if i == 0:
	print("none")
else:
	print(bus_numbers[i - 1])
