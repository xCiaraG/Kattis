n, m = [int(x) for x in input().split()]
to_translate = set(input().split())
translators = {"English": set()}
for _ in range(m):
	translation = input().split()
	a, b, cost = translation[0], translation[1], int(translation[2])
	if a not in translators:
		translators[a] = set([(cost, b)])
	else:
		translators[a].add((cost, b))
	if b not in translators:
		translators[b] = set([(cost, a)])
	else:
		translators[b].add((cost, a))

cost = 0
current = set(["English"])
change = True
while to_translate and change:
	change = False
	to_check = []
	for c in current:
		to_check += list(translators[c])
	to_check = sorted(to_check)
	for t in to_check:
		if t[1] in to_translate:
			cost += t[0]
			change = True
			to_translate.remove(t[1])
			current.add(t[1])

if to_translate:
	print("Impossible")
else:
	print(cost)