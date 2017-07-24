mport sys
line = list(map(int, sys.stdin.readline().strip().split()))
score = line[1] + line[2]
if score//line[0] % 2 == 0:
    server = "paul"
else:
    server = "opponent"
print(server)
