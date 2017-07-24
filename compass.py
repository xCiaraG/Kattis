import sys
n1 = int(sys.stdin.readline().strip())
n2 = int(sys.stdin.readline().strip())

if n1 - n2 == -180 or n1 - n2 == 180:
    print(180)
elif n1 > n2 and 360 - n1 + n2 < 180:
    print(360 - n1 + n2)
elif n1 > n2:
    print(-(n1-n2))
elif n2-n1 < 180:
    print(n2-n1)
else:
    print(-360 -n1 + n2)
