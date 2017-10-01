from sys import stdin
t = int(stdin.readline())
for i in range(0, t):
    n, m, l = [int(x) for x in stdin.readline().split()]
    d = {}
    for j in range(1, n+1):
        d[j] =[]

    for j in range(0, m):
        n1, n2 = [int(x) for x in stdin.readline().split()]
        d[n1].append(n2)

    to_check = []
    knocked = []
    for j in range(0, l):
        to_check.append(int(stdin.readline()))
        knocked += to_check
        while to_check:
            for n in to_check[:]:
                if d[n]:
                    to_check += d[n]
                    knocked += d[n]
                    d[n] = []
                to_check.remove(n)
    print(len(set(knocked)))