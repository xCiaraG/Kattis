import sys
line = sys.stdin.readline().strip()
d = {}
count = 0
for letter in line:
    if letter not in d:
        d[letter] = 1
    else:
        d[letter] += 1

while len(d) > 2:
    miniumum = min(d.values())
    miniumum_key = ""
    for key in d:
        if d[key] == miniumum:
            miniumum_key = key
    count += miniumum
    del d[miniumum_key]

print(count)
