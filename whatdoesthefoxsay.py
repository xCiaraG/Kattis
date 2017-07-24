import sys
n = int(sys.stdin.readline().strip())
for i in range(0,n):
    line = sys.stdin.readline().strip()
    words = line.split()
    animals = []
    while line != "what does the fox say?":
        line = sys.stdin.readline().strip()
        animal = line.split()
        animals.append(animal[2])
    s = ""
    for noise in words:
        if noise not in animals:
            s += noise + " "
    print(s.strip())
