mport sys
n = int(sys.stdin.readline().strip())
for i in range(0, n):
    line = sys.stdin.readline()
    line = sys.stdin.readline()
    godzilla = list(map(int, sys.stdin.readline().strip().split()))
    mechagodzilla = list(map(int, sys.stdin.readline().strip().split()))
    if max(mechagodzilla) > max(godzilla):
        print("MechaGodzilla")
    else:
        print("Godzilla")
