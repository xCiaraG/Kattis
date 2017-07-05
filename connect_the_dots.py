import sys

def go_up(image, x1, y1, x2):
    while x1 > x2:
        x1 -= 1
        if image[x1][y1] == ".":
            image[x1][y1] = "|"
        elif image[x1][y1] == "-":
            image[x1][y1] = "+"
    return image

def go_down(image, x1, y1, x2):
    while x1 < x2:
        x1 += 1
        if image[x1][y1] == ".":
            image[x1][y1] = "|"
        elif image[x1][y1] == "-":
            image[x1][y1] = "+"
    return image

def go_left(image, x1, y1, y2):
    while y1 > y2:
        y1 -= 1
        if image[x1][y1] == ".":
            image[x1][y1] = "-"
        elif image[x1][y1] == "|":
            image[x1][y1] = "+"
    return image

def go_right(image, x1, y1, y2):
    while y1 < y2:
        y1 += 1
        if image[x1][y1] == ".":
            image[x1][y1] = "-"
        elif image[x1][y1] == "|":
            image[x1][y1] = "+"
    return image

def find_position(pos, image):
    global a, b
    i = 0
    while i < a:
        j = 0
        while j < b:
            if sequence[pos] == image[i][j]:
                return i, j
            j += 1
        i += 1

def find_position2(letter, x, y):
    global a, b
    tmpx = x + 1
    tmpy = y + 1
    while tmpx < a:
        if letter == image[tmpx][y]:
            return tmpx, y
        tmpx += 1

    tmpx = x - 1
    while tmpx > -1:
        if letter == image[tmpx][y]:
            return tmpx, y
        tmpx -=1 

    while tmpy < b:
        if letter == image[x][tmpy]:
            return x, tmpy
        tmpy += 1

    tmpy = y - 1
    while tmpy > -1:
        if letter == image[x][tmpy]:
            return x, tmpy
        tmpy -= 1

def process_image(image):
    global a, b
    m = 0
    for line in image:
        for c in line:
            if c in sequence and sequence.index(c) > m:
                m = sequence.index(c)
    a = len(image)
    b = len(image[0])
    pos = 0
    if pos < m:
        x1, y1 = find_position(pos, image)
    while pos < m:
        x2, y2 = find_position2(sequence[pos+1], x1, y1)
        if x1 > x2: 
            image = go_up(image, x1, y1, x2)
        elif x1 < x2:
            image =  go_down(image, x1, y1, x2)
        elif y1 > y2:
            image = go_left(image, x1, y1, y2)
        else:
            image = go_right(image, x1, y1, y2)
        pos += 1
        x1, y1 = x2, y2
    for line in image:
        print("".join(line))

sequence = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
lines = sys.stdin.readlines()
image = []
for line in lines:
    if line != "\n":
        line = list(line)
        if line[-1] == "\n":
            line = line[:-1]
        image.append(line)
    else:
        process_image(image)
        image = []
        print()
if image:
    process_image(image)