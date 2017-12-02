start_x, start_y = [int(x) for x in input().split()]
end_x, end_y = [int(x) for x in input().split()]
distance = abs(start_x - end_x) + abs(start_y - end_y)
fuel = int(input())
if distance > fuel:
	print("N")
elif (fuel - distance) % 2 == 0:
	print("Y")
else:
	print("N")