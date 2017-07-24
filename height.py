n = int(input())
for i in range(0, n):
    line = list(map(int, input().strip().split()))
    tmp3 = line[0]
    new = [line[1]]
    line = line[2:]
    total = 0
    for student in line:
        i = 0
        while i < len(new) and new[i] < student:
            i += 1
        total += len(new) - i
        if i < len(new):
            tmp = new[i]
            new[i] = student
            i += 1
            a = True
        else:
            a = False
            new.append(student)
        while i < len(new) and a:
            tmp2 = new[i]
            new[i] = tmp
            tmp = tmp2
            i += 1
        if a:
            new.append(tmp)
    print(tmp3, total)

