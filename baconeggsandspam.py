import sys
n = int(sys.stdin.readline().strip())
while n != 0:
    d = {}
    for i in range(0, n):
        line = sys.stdin.readline().strip().split()
        customer = line[0]
        line.remove(customer)
        for food in line:
            if food not in d:
                d[food] = [customer]
            else:
                d[food].append(customer)

    for food in sorted(d):
        s = "" + food + " "
        s += " ".join(sorted(d[food]))
        print(s)
    print()
    n = int(sys.stdin.readline().strip())
