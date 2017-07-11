line = list(map(int, input().strip().split()))
problems =  list(map(int, input().strip().split()))
time = 300 
total = 0
count = 0

if 300 - problems[line[1]] >= 0:
    time -= problems[line[1]]
    total += problems[line[1]]
    count += 1
    problems.remove(problems[line[1]])
    problems = sorted(problems)

    while problems and time - problems[0] >= 0:
        count += 1
        time -= problems[0]
        total += 300 - time
        problems.remove(problems[0])

print(count, total)