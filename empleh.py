white = input().strip().split()
if len(white) > 1:
    white = white[1].strip().split(",")
else:
    white = False
black = input().strip().split()
if len(black) > 1:
    black = black[1].strip().split(",")
else:
    black = False
divider = "+---+---+---+---+---+---+---+---+"
current = "."
print(divider)
for i in range(8, 0, -1):
    s = "|"
    for letter in "abcdefgh":
        tmp = letter + str(i)
        a = False
        if white:
            for pos in white:
                if tmp in pos:
                    if len(pos) == 3:
                        to_place = pos[0]
                    else:
                        to_place = "p"
                    a = True
        if black:
            for pos in black:
                if tmp in pos:
                    if len(pos) == 3:
                        to_place = pos[0].lower()
                    else:
                        to_place = "p"
                    a = True

        if a:
            s += current + to_place + current + "|"
            #print(tmp, to_place)
        else:
            s += current*3 + "|"
        if current == ".":
            current = ":"
        else:
            current = "."
    if current == ".":
        current = ":"
    else:
        current = "."
    print(s)
    print(divider)
