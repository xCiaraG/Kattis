import sys
line1 = sys.stdin.readline().strip()
line2 = sys.stdin.readline().strip()
if len(line1) < len(line2):
    print("no")
else:
    print("go")
