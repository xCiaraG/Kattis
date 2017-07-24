import sys
lines = sys.stdin.readlines()
for line in lines:
    line = line.strip().lower()
    if "problem" in line:
        print("yes")
    else:
        print("no")
