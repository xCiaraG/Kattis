import sys
scores = {"A":11,"K":4,"Q":3,"J":2,"T":10,"9":0,"8":0,"7":0}
line = sys.stdin.readline().strip().split()
n = int(line[0])
dominant = line[1]
total = 0
for i in range(0,4*n):
    line = sys.stdin.readline().strip()
    if line[1] == dominant and line[0] == "J":
        total += 20
    elif line[1] == dominant and line[0] == "9":
        total += 14
    else:
        total += scores[line[0]]
print(total)
