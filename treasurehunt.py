line = list(map(int, input().strip().split()))
treasure_map = []
for i in range(0, line[0]):
    treasure_map.append(list(input().strip()))
count = 0
i = 0
j = 0
li = len(treasure_map)
lj = len(treasure_map[0])
play = treasure_map[i][j]
while play != "T" and -1 < i < li and -1 < j < lj:
    play = treasure_map[i][j]
    treasure_map[i][j] = "D"
    if play == "N":
        i -= 1
    elif play   == "S":
        i += 1
    elif play   == "E":
        j += 1
    elif play   == "W":
        j -= 1
    elif play != "T":
        i = -1
        j = -1
    count += 1

if i == -1 and j == -1:
    print("Lost")
elif -1 == i or i == li or -1 == j or j == lj:
    print("Out")
else:
    if count == 0:
        print(count)
    else:
        print(count-1)