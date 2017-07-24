import sys
n = int(sys.stdin.readline().strip())
for i in range(0,n):
    m = int(sys.stdin.readline().strip())
    total_votes = 0
    maximum_vote = 0
    winners = []
    for j in range(0,m):
        vote = int(sys.stdin.readline().strip())
        if vote > maximum_vote:
            maximum_vote = vote
            winners = [j+1]
        elif vote == maximum_vote:
            winners.append(j+1)
        total_votes += vote
    if len(winners) > 1:
        print("no winner")
    elif total_votes//2 < maximum_vote:
        print("majority winner", winners[0])
    else:
        print("minority winner", winners[0])
