import sys
n = int(sys.stdin.readline().strip())
line1 = sys.stdin.readline().strip()
line2 = sys.stdin.readline().strip()

if n % 2 != 0:
    s = ""
    for d in line1:
        if d == "0":
            s += "1"
        else:
            s += "0"

if (n % 2 == 0 and line1 == line2) or (n%2 == 1 and line2 == s):
    print("Deletion succeeded")
else:
    print("Deletion failed")
