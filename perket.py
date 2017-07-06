import itertools
n = int(input().strip())
ingredients = []
for i in range(0, n):
    line = list(map(int, input().strip().split()))
    ingredients.append([line[0], line[1]])
l = len(ingredients)
a = []
for i in range(1, l+1):
    a = a + list(itertools.combinations(ingredients, i))
new = []
for t in a:
    x = 1
    y = 0
    for l in t:
        x *= l[0]
        y += l[1]
    new.append(abs(x-y))
print(min(new))