n = int(input())
ingredients = set()
t = 0
for i in range(n):
	recipe = set([int(x) for x in input().split()][1:])
	if not recipe.intersection(ingredients):
		t += 1
		ingredients = ingredients.union(recipe)
print(t)
