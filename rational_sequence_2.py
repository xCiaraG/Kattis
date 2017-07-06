n = int(input().strip())
for i in range(0, n):
    line = input().strip().split()
    tmp = line[1].split("/")
    x = int(tmp[0])
    y = int(tmp[1])
    ans = ""
    while x != 1 or y != 1:
        if x < y:
            y -= x
            ans = "0" + ans
        else:
            x -= y
            ans = "1" + ans
    ans = "1" + ans
    print("{} {}".format(line[0], int(ans, 2)))