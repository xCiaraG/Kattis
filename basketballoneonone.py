from sys import stdin

def find_winner(scores):
	a, b  = 0, 0
	for i in range(0, len(scores), 2):
		if scores[i] == "A":
			a += int(scores[i+1])
		else:
			b += int(scores[i+1])
		if a >= 11 and a > b and (a-b) > 1:
			return "A"
		elif b >= 11 and b > a and (b-a) > 1:
			return "B"

scores = stdin.readline().strip()
print(find_winner(scores))