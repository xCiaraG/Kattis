import sys,math
lines = sys.stdin.readlines()
for line in lines:
    line = line.strip()
    letters = {}
    for c in line:
        if c not in letters:
            letters[c] = 1
        else:
            letters[c] += 1
    t = 1
    s = 0
    for key in letters:
        tmp = math.factorial(letters[key])
        t = t * tmp
        s += letters[key]
    print(math.factorial(s)//t) 