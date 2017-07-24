import sys
name = sys.stdin.readline().strip()
while name != "0":
    d = {}
    student_go = {}
    while name != "1":
        d[name] = 0
        count = 0
        line = sys.stdin.readline().strip()
        while line[0] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ1":
            d[name] += 1
            if line not in student_go:
                student_go[line] = [name]
            else:
                if name not in student_go[line]:
                    student_go[line].append(name)
                else:
                    d[name] -= 1
            line = sys.stdin.readline().strip()
        name = line
    for student in student_go:
        if len(student_go[student]) > 1:
            for company in student_go[student]:
                d[company] -= 1
    projects = []
    for key in d:
        projects.append((d[key], key))
    projects = sorted(projects)
    projects.reverse()
    i = 0 
    to_sort = []
    while i < len(projects):
        if i + 1 < len(projects) and projects[i][0] == projects[i+1][0]:
            to_sort.append((projects[i][1], projects[i][0]))
        else:
            to_sort.append((projects[i][1], projects[i][0]))
            to_sort = sorted(to_sort)
            for project in to_sort:
                print("{} {}".format(project[0], project[1]))
            to_sort = []
        i += 1
    name = input().strip()
