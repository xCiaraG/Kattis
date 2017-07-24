import sys
n = int(sys.stdin.readline().strip())
for i in range(0, n):
    line = sys.stdin.readline().strip().split()
    if int(line[1][:4]) >= 2010 or int(line[2][:4]) >= 1991:
        print(line[0], "eligible")
    elif int(line[3]) >= 41:
        print(line[0], "ineligible")
    else:
        print(line[0], "coach petitions")
