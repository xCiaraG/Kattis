line = input().strip()
rank, stars, conseq = 25, 0, 0
rankings = {1:5, 2:5, 3:5, 4:5, 5:5, 6:5, 7:5, 8:5, 9:5, 10:5, 11:4, 12:4, 13:4, 14:4, 15:4, 16:3, 17:3, 18:3, 19:3, 20:3, 21:2, 22:2, 23:2, 24:2, 25:2}
for result in line:
	if result == "W":
		if 6 <= rank:
			conseq += 1
		else:
			conseq = 0
		if conseq > 2:
			stars += 2
		else:
			stars += 1
	else:
		if rank <= 20:
			stars -= 1
		conseq = 0
	if stars == -1:
		if rank == 20:
			stars = 0
		else:
			rank += 1
			stars = rankings[rank] - 1
	elif stars > rankings[rank]:
		stars -= rankings[rank]
		rank -= 1 
	if rank == 0:
		rank = "Legend"
		break
print(rank)
