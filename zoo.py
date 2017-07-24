import sys
n = int(sys.stdin.readline().strip())
count = 1
while n != 0:
    d = {}
    for i in range(0, n):
        animal = sys.stdin.readline().strip().split()
        animal = animal[-1].lower()
        if animal not in d:
            d[animal] = 1
        else:
            d[animal] += 1
    print("List {}:".format(count))
    for (k, v) in sorted(d.items()):
        print("{} | {}".format(k,v))
    count += 1
    n = int(sys.stdin.readline().strip())
