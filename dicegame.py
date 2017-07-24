dice1 = list(map(int, input().strip().split()))
dice2 = list(map(int, input().strip().split()))
d1 = []
d2 = []
for i in range(dice1[0], dice1[1] + 1):
    for j in range(dice1[2], dice1[3] + 1):
        d1.append(i + j)
for i in range(dice2[0], dice2[1] + 1):
    for j in range(dice2[2], dice2[3] + 1):
        d2.append(i + j)

d1 = sorted(d1)
d2 = sorted(d2)

if sum(d1)/len(d1) > sum(d2)/len(d2):
    print("Gunnar")
elif sum(d2)/len(d2) > sum(d1)/len(d1):
    print("Emma")
else:
    print("Tie")
