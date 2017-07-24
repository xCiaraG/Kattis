import sys
lines = sys.stdin.readlines()
for line in lines:
    line = line.strip().split()
    time1 = list(map(int, line[3].split(":")))
    time2 = list(map(int, line[4].split(":")))
    if time2[1] == time1[1]:
        line[3] = "{} hours".format(time2[0]-time1[0])
        line[4] = "0 minutes"
    elif time2[1] > time1[1]:
        line[3] = "{} hours".format(time2[0]-time1[0])
        line[4] = "{} minutes".format(time2[1]-time1[1])
    else:
        t1 = time1[1]-time2[1]
        line[3] = "{} hours".format(time2[0]-time1[0]-1)
        line[4] = "{} minutes".format(60 - t1)
    print(" ".join(line))
