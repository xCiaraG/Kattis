import sys
n = int(sys.stdin.readline().strip())
for i in range(0, n):
    line1 = sys.stdin.readline().strip()
    line2 = sys.stdin.readline().strip()
    s = ""
    j = 0
    while j < len(line1):
        if line1[j] == line2[j]:
            s += "."
        else:
            s += "*"
        j += 1
    print(line1)
    print(line2)
    print(s + "\n")
