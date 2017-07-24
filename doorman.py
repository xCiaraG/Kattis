import sys
n = int(sys.stdin.readline().strip())
line = sys.stdin.readline()
count = 0
tracker = 0
tmp = []
a = True
for person in line:
    if a and person == "M" and tracker > -n:
        count += 1
        tracker -= 1
    elif a and person == "W" and tracker < n:
        count += 1
        tracker += 1
    elif a and not tmp:
        tmp.append(person)
    elif a and person != tmp[0]:
        if tmp[0] == "M":
            tracker -= 1
        else:
            tracker += 1
        count += 1
        tmp[0] = person
    else:
        a = False
print(count)
