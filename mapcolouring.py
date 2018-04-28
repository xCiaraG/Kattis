from collections import defaultdict
from sys import stdin

def dfs(i, colours, min_found):  
    if i == C:
        return min(min_found, max(colours))

    current = set([colours[j] for j in borders[i] if colours[j]])
    if max(colours) >= min_found:
        return min_found
    for j in range(1, 5):
        if j not in current:
            colours[i] = j
            min_found = min(min_found, dfs(i + 1, colours, min_found))
            colours[i] = 0
    return min_found

T = int(input())
for _ in range(T):
    C, B = [int(x) for x in stdin.readline().split()]
    borders = defaultdict(list)
    for _ in range(B):
        i, j = [int(x) for x in stdin.readline().split()]
        borders[i].append(j)
        borders[j].append(i)

    min_found = 5
    colours = [1] + [0]*(C - 1)
    if B == 0:
        min_found = 1
    else:
        min_found = dfs(1, colours, min_found)

    if min_found > 4:
        print('many')
    else:
        print(min_found)
