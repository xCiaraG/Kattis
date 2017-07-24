n = list(map(int, input().strip().split()))
while n != [0, 0]:
    new = []
    line = input()
    for letter in line:
        new.append(letter)
    for i in range(1, n[0]):
        line = input()
        j = 0
        while j < len(line):
            new[j] += line[j]
            j += 1
    new = sorted(new, key=lambda s: s.lower())
    for i in range(0, n[0]):
        s = ""
        for j in range(0, n[1]):
            s += new[j][i]
        print(s)
    n = list(map(int, input().strip().split()))
    if n != [0, 0]:
        print()
