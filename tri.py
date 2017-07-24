import sys
line = list(map(int, sys.stdin.readline().strip().split()))
if line[0] + line[1] == line[2]:
    print(str(line[0]) + "+" + str(line[1]) + "=" + str(line[2]))
elif line[0] - line[1] == line[2]:
    print(str(line[0]) + "-" + str(line[1]) + "=" + str(line[2]))
elif line[0] * line[1] == line[2]:
    print(str(line[0]) + "*" + str(line[1]) + "=" + str(line[2]))
elif line[0] / line[1] == line[2]:
    print(str(line[0]) + "/" + str(line[1]) + "=" + str(line[2]))
elif line[0] == line[1] + line[2]:
    print(str(line[0]) + "=" + str(line[1]) + "+" + str(line[2]))
elif line[0] == line[1] - line[2]:
    print(str(line[0]) + "=" + str(line[1]) + "-" + str(line[2]))
elif line[0] == line[1] * line[2]:
    print(str(line[0]) + "=" + str(line[1]) + "*" + str(line[2]))
elif line[0] == line[1] / line[2]:
    print(str(line[0]) + "=" + str(line[1]) + "/" + str(line[2]))
