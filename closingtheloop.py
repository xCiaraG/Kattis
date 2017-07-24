import sys
n = int(sys.stdin.readline().strip())
for i in range(0, n):
    num_rope = int(sys.stdin.readline().strip())
    blue = []
    red = []
    length = 0
    line = sys.stdin.readline().strip().split()
    for rope in line:
        if rope[len(rope)-1:len(rope)] == "B":
            blue.append(int(rope[:len(rope)-1]))
        else:
            red.append(int(rope[:len(rope)-1]))
    red = sorted(red)
    blue = sorted(blue)
    tmp = False
    if len(blue) == len(red):
        tmp = True
    if len(blue) > len(red):
        start = blue
    else:
        start = red
    while red and blue:
        length += start.pop() - 1
        if start == blue:
            start = red
        else:
            start = blue
    if tmp:
        length += start.pop() - 1
    print("Case #{}: {}".format(i + 1, length))
