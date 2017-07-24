import sys
dwarfs = []
for i in range(0, 9):
    dwarfs.append(int(sys.stdin.readline().strip()))

total = sum(dwarfs)
a = True
i = 0
while i < len(dwarfs) and a:
    j = i + 1
    while j < len(dwarfs) and a:
        if total - dwarfs[i] - dwarfs[j] == 100:
            a = False
            non_dwarfs = [dwarfs[i], dwarfs[j]]
        j += 1
    i += 1
for dwarf in dwarfs:
    if dwarf not in non_dwarfs:
        print(dwarf)
