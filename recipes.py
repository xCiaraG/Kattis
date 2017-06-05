n = int(input())
for i in range(0, n):
	line = list(map(int, input().strip().split()))
	m = line[0]
	scale = line[2]/line[1]
	ingredients = []
	for j in range(0, m):
		line = input().strip().split()
		if float(line[2]) == 100:
			scaled_weight = float(line[1])*scale
		ingredients.append(line)
	print("Recipe # {}".format(i+1))
	for ingredient in ingredients:
		print("{} {}".format(ingredient[0], (float(ingredient[2])/100)*scaled_weight))
	print("-"*40)