mport sys
numbers = list(map(int, sys.stdin.readline().strip().split()))
bricks = list(map(int, sys.stdin.readline().strip().split()))
pos_bricks = 0
a = True
for i in range(0, numbers[0]):
    width = 0
    while width < numbers[1]:
        width += bricks[pos_bricks]
        pos_bricks += 1
    if width != numbers[1]:
        a = False

if a:
    print("YES")
else:
    print("NO")
