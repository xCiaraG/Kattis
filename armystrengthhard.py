from sys import stdin
n = int(stdin.readline().strip())
for i in range(0, n):
    line = stdin.readline()
    line = stdin.readline()
    godzilla = [int(x) for x in stdin.readline().split()]
    mechagodzilla = [int(x) for x in stdin.readline().split()]
    if max(mechagodzilla) > max(godzilla):
        print("MechaGodzilla")
    else:
        print("Godzilla")