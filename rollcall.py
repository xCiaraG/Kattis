import sys
names = []
d = {}
lines = sys.stdin.readlines()
for name in lines:
    name = name.strip().split()
    if name[0] not in d:
        d[name[0]] = 1
    else:
        d[name[0]] += 1
    names.append((name[1], name[0]))

names = sorted(names)
for name in names:
    if d[name[1]] > 1:
        print(name[1], name[0])
    else:
        print(name[1])
