import sys
n = int(sys.stdin.readline().strip())
while n != 0:
    am = []
    pm = []
    for i in range(0, n):
        line = sys.stdin.readline().strip().split()
        time = line[0].split(":")
        time[0] = int(time[0])
        time[1] = int(time[1])
        if time[0] == 12:
            time[0] = -1
        if line[1] == "a.m.":
            am.append(time)
        else:
            pm.append(time)
    am = sorted(am)
    pm = sorted(pm)
    for time in am:
        if time[0] == -1:
            time[0] = 12
        if len(str(time[1])) == 1:
            time[1] = "0" + str(time[1])
        print("{}:{} a.m.".format(time[0], time[1]))
    for time in pm:
        if time[0] == -1:
            time[0] = 12
        if len(str(time[1])) == 1:
            time[1] = "0" + str(time[1])
        print("{}:{} p.m.".format(time[0], time[1]))
    n = int(sys.stdin.readline().strip())
    if n != 0:
        print()
