import math
circle = "ABCDEFGHIJKLMNOPQRSTUVWXYZ '"

def distance(l1, l2):
	return min(((circle.index(l2) - circle.index(l1)) % 28), ((circle.index(l1) - circle.index(l2)) % 28))

n = int(input())
for i in range(n):
	sentence = input().strip()
	total = 0
	current = sentence[0]
	for letter in sentence[1:]:
		total += distance(current, letter)
		current = letter

	print(((math.pi * 60) / 28 / 15 * total) + len(sentence))