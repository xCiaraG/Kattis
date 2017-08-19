from sys import stdin
def beats(x, y):
	return x + y in ["rockscissors", "paperrock", "scissorspaper"]

line = [int(x) for x in stdin.readline().split()]
while line != [0]:
	n, k = line[0], line[1]
	scores = []
	for i in range(0, n):
		scores.append([0, 0])
	for i in range(0, ((n*k)*(n-1))//2):
		game = stdin.readline().split()
		if beats(game[1], game[3]):
			scores[int(game[0])-1][0] += 1
			scores[int(game[0])-1][1] += 1
			scores[int(game[2])-1][1] += 1
		elif beats(game[3], game[1]):
			scores[int(game[2])-1][0] += 1
			scores[int(game[0])-1][1] += 1
			scores[int(game[2])-1][1] += 1
	for score in scores:
		if score[1] != 0:
			print("{:.3f}".format(float(score[0])/float(score[1])))	
		else:
			print("-")
	line = [int(x) for x in stdin.readline().split()]
	if line != [0]:
		print("")

