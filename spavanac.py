import sys
time = list(map(int, sys.stdin.readline().strip().split()))
if time[1] >= 45:
    print(time[0], time[1]-45)
elif time[0] == 0:
    tmp = 45 - time[1]
    print(23, 60 - tmp)
else:
    tmp = 45 - time[1]
    print(time[0]-1, 60 - tmp)
