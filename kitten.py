def find_journey(checked, journey):
	if kitten not in branches[journey[-1]]:
		for p in branches[journey[-1]]:
			if p not in checked and p in branches:
				find_journey(checked + [p], journey + [p])
	else:
		journey.append(kitten)
		print(*journey[::-1	])


kitten = int(input())
branch = [int(x) for x in input().split()]
root = branch[0]
branches = {}
while branch != [-1]:
	branches[branch[0]] = branch[1:]
	branch = [int(x) for x in input().split()]

find_journey([root], [root])

