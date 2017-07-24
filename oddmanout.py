import sys
n = int(sys.stdin.readline().strip())
for i in range(0, n):
    m = int(sys.stdin.readline().strip())
    line = list(map(int, sys.stdin.readline().strip().split()))
    line = sorted(line)
    k = 0
    odd_man = ""
    while k < len(line):
        if k < len(line) - 1 and line[k] != line[k+1]:
            odd_man = line[k]
            k += 1
        else:
            k += 2
    if not odd_man:
        odd_man = line[len(line)-1]
    print("Case #{}: {}".format(i+1, odd_man))
