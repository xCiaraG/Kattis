n = int(input())
for i in range(0, n):
    m = list(map(int, input().strip().split()))
    tickets = {}
    need = []
    total = 0
    for j in range(0, m[0]):
        line = list(map(int, input().strip().split()))
        need.append((line[1:-1],line[-1]))
    line = list(map(int, input().strip().split()))
    k = 0
    while k < len(line):
        tickets[k+1] = line[k]
        k += 1
    for t in need:
        m = tickets[t[0][0]]
        for k in range(1, len(t[0])):
            if tickets[t[0][k]] < m:
                m = tickets[t[0][k]]
        total += m*t[1]
    print(total)
