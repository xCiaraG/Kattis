import math
def width(t, P):
    tmp = (9/16)*t*P
    return math.ceil(tmp)

def height(Cw, Cmax):
    tmp = 8 + ((40*(Cw-4))/(Cmax-4))
    return math.ceil(tmp)

k = 1
n = list(map(int, input().strip().split()))
while n != [0, 0]:
    total = 0
    row_width = n[0]
    d = {}
    words = []
    m = 0
    for i in range(0, n[1]):
        word = input().strip().split()
        if int(word[1]) >= 5:
            words.append(word[0])
            d[word[0]] = int(word[1])
            if int(word[1]) > m:
                m = int(word[1])
    words = sorted(words)
    tmp_width = row_width
    mheight = 0
    for word in words:
        h = height(d[word], m)
        w = width(len(word), h)
        if tmp_width - w >= 0:
            if h > mheight:
                mheight = h
            tmp_width -= (w + 10)
        else:
            total += mheight
            mheight = h
            tmp_width = row_width - w - 10
    total += mheight
    print("CLOUD {}: {}".format(k,total))
    n = list(map(int, input().strip().split()))
    k += 1