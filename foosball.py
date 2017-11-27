n = int(input())
players = input().split()
W1, B1, W2, B2 = players[0], players[1], players[2], players[3]
players = players[4:]
play = input().strip()
d_players, d_score, d_team = [], 0, ""
current_d, current_play = 1, play[0]
pw, pb = [W1, W2], [B1, B2]
for p in play[1:]:
	if current_play == p:
		current_d += 1
	else:
		if current_d > d_score:
			d_score = current_d
			d_team = current_play
			if current_play == "W":
				d_players = pw
			else:
				d_players = pb
		elif current_d == d_score:
			d_team += current_play
			if current_play == "W":
				d_players += pw
			else:
				d_players += pb
		current_d = 1
	if current_play == "W":
		W1, W2 = W2, W1
		players.append(B2)
		B1, B2 = players.pop(0), B1
		pb = [B2, B1]
	else:
		B1, B2 = B2, B1
		players.append(W2)
		W1, W2 = players.pop(0), W1
		pw = [W2, W1]
	current_play = p

if current_d > d_score:
	d_score = current_d
	d_team = current_play
	if current_play == "W":
		d_players = pw
	else:
		d_players = pb
elif current_d == d_score:
	d_team += current_play
	if current_play == "W":
		d_players += pw
	else:
		d_players += pb

for i in range(0, len(d_players), 2):
	print(d_players[i], d_players[i+1])



