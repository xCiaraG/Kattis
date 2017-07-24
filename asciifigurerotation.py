n = int(input())
while n != 0:
    picture = []
    for i in range(0, n):
        picture.append(input().rstrip())
    i = 0
    while i < len(picture):
        picture[i] += " "*(len(max(picture, key=len))-len(picture[i]))
        i += 1
    new_picture = [""]*len(picture[0])
    i = len(picture)-1
    while i != -1:
        j = 0
        while j < len(picture[i]):
            if picture[i][j] == "-":
                new_picture[j] += "|"
            elif picture[i][j] == "|":
                new_picture[j] += "-"
            else:
                new_picture[j] += picture[i][j]
            j += 1
        i -= 1
    for l in new_picture:
        if l:
            print(l.rstrip())
    n = int(input())
    if n != 0:
        print()