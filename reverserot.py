import sys
def rotate(letter, n):
    alphabeth = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    i = 0
    while alphabeth[i] != letter:
        i += 1
    pos = (i +n) % len(alphabeth)
    return alphabeth[pos]

line = sys.stdin.readline().strip().split()
while line != ["0"]:
    s = ""
    for letter in line[1][::-1]:
        s += rotate(letter, int(line[0]))
    print(s)
    line = sys.stdin.readline().strip().split()
