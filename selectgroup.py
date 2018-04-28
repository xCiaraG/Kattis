from sys import stdin
groups = {}
for line in stdin.readlines():
    line = line.strip().split()
    if line[0] == 'group':
        groups[line[1]] = set(line[3:])
    else:
        for i in range(len(line)):
            if line[i] in groups:
                line[i] = groups[line[i]]
        i = 0
        line = line[::-1]
        while i < len(line):
            if line[i] in ['union', 'intersection', 'difference']:
                if line[i] == 'union':
                    line[i] = line[i - 1].union(line[i - 2])
                elif line[i] == 'intersection':
                    line[i] = line[i - 1].intersection(line[i - 2])
                else:
                    line[i] = line[i - 1] - line[i - 2]
                line.pop(i - 1)
                line.pop(i - 2)
                i -= 1
            else:
                i += 1
        print(*sorted(list(line[0])))