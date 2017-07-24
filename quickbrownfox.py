import sys
n = int(sys.stdin.readline().strip())
for i in range(0, n):
    line = sys.stdin.readline().strip()
    tmp = ""
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter not in line and letter.upper() not in line:
            tmp += letter
    if not tmp:
        print("pangram")
    else:
        print("missing " + tmp)
