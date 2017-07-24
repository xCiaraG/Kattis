import sys
rooms = list(map(int,sys.stdin.readline().strip().split()))
r = []
for i in range(0, rooms[1]):
    room = int(sys.stdin.readline().strip())
    r.append(room)
if rooms[0] == rooms[1]:
    print("too late")
else:
    a = True
    i = 1
    while a:
        if i not in r:
            print(i)
            a = False
        i += 1
