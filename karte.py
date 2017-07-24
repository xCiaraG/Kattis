import sys
line = sys.stdin.readline().strip()
i = 0
cards = []
while i < len(line)-2:
    cards.append(line[i:i+3])
    i += 3
p, k ,h, t = 13, 13, 13, 13
for card in cards:
    if card[0] == "P":
        p -= 1
    elif card[0] == "K":
        k -= 1
    elif card[0] == "H":
        h -= 1
    elif card[0] == "T":
        t -= 1
l = len(cards)
tmp = set(cards)
if len(tmp) < l:
    print("GRESKA")
else:
    print("{} {} {} {}".format(p,k,h,t))
