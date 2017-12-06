n = int(input())
cards = [int(x) for x in input().split()]
move = True
while move:
	move = False
	i = 0
	while i < len(cards) - 1:
		if cards[i] % 2 == cards[i+1] % 2:
			cards.pop(i)
			cards.pop(i)
			move = True
		else:
			i += 1
print(len(cards))