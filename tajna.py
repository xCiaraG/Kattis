word = input().strip()
length = len(word)
possible = []
for i in range(1, length):
    if length % i == 0:
        possible.append((i, length//i))

a = True
i = -1
while a:
    if possible[i][0] <= possible[i][1]:
        actual = possible[i]
        a = False
    i -= 1
m = []
i = 0
for j in range(0, actual[1]):
    to_place = []
    for k in range(0, actual[0]):
        to_place.append(word[i])
        i += 1
    m.append(to_place)

w = ""
for i in range(0, actual[0]):
    for part in m:
        w += part[i]
print(w)
