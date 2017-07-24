import sys
line = list(map(int, sys.stdin.readline().strip().split()))
while line != [0,0]:
    if line[0] + line[1] == 13:
        print("Never speak again.")
    elif line[1] > line[0]:
        print("Left beehind.")
    elif line[1] < line[0]:
        print("To the convention.")
    else:
        print("Undecided.")
    line = list(map(int, sys.stdin.readline().strip().split()))
