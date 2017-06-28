line = list(map(int, input().strip().split()))
while line != [0, 0, 0, 0]:
   player1 = sorted([line[0], line[1]])
   player2 = sorted([line[2], line[3]])
   
   if player1[0] == 1 and player1[1] == 2:
      p1 = (1, 0) 
   elif player1[0] == player1[1]:
      p1 = (2, player1[0])
   else:
      p1 = (3, int("".join([str(player1[1]), str(player1[0])])))
   
   if player2[0] == 1 and player2[1] == 2:
      p2 = (1, 0)
   elif player2[0] == player2[1]:
      p2 = (2, player2[0])
   else:
      p2 = (3, int("".join([str(player2[1]), str(player2[0])])))

   if p1 == p2:
      print("Tie.")
   elif p1[0] < p2[0] or (p1[0] == p2[0] and p1[1] > p2[1]):
      print("Player 1 wins.")
   else:
      print("Player 2 wins.")
   line = list(map(int, input().strip().split()))