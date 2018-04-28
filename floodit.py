from sys import stdin
from collections import deque

def main():
    T = int(stdin.readline().strip())
    for _ in range(T):
        n = int(stdin.readline().strip())
        t, total = 0, n**2 - 1
        board = [[int(x) for x in list(stdin.readline().strip())] for _ in range(n)]
        sizes = [[0 for _ in range(n)] for _ in range(n)]
        colours = [0, 0, 0, 0, 0, 0, 0]
        iterations = 0
        groups = {}
     
        #INITIATE FLOOD
        flooded = set([(0, 0)])
        to_check = deque([(0, 0)])
        while to_check:
            a, b = to_check.popleft()
            for c, d in [(a + 1, b), (a - 1, b), (a, b + 1), (a, b - 1)]:
                if 0 <= c < n and 0 <= d < n and board[a][b] == board[c][d] and (c, d) not in flooded:
                    t += 1
                    to_check.append((c, d))
                    flooded.add((c, d))
     
        #GROUP NUMS
        seen = [[True for _ in range(n)] for _ in range(n)]
        x = 0
        for i in range(n):
            for j in range(n):
                if seen[i][j]:
                    x += 1
                    seen[i][j] = False
                    to_check = deque([(i, j)])
                    current = []
                    count = 0
                    while to_check:
                        count += 1
                        a, b = to_check.popleft()
                        current.append((a, b))
                        for c, d in [(a + 1, b), (a - 1, b), (a, b + 1), (a, b - 1)]:
                            if 0 <= c < n and 0 <= d < n and board[a][b] == board[c][d] and seen[c][d]:
                                to_check.append((c, d))
                                seen[c][d] = False
                for a, b in current:
                    sizes[a][b] = (count, x)
                groups[x] = current
     
        while t < total:
            iterations += 1
            counts = [0, 0, 0, 0, 0, 0, 0]
            index_to_fill = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}
            #FIND BIGGEST
            seen_ids = set()
            for i, j in flooded:
                for a, b in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= a < n and 0 <= b < n and sizes[a][b][1] not in seen_ids and (a, b) not in flooded:
                        counts[board[a][b]] += sizes[a][b][0]
                        seen_ids.add(sizes[a][b][1])
                        index_to_fill[board[a][b]].append(sizes[a][b][1])
            to_fill = counts.index(max(counts))
            colours[to_fill] += 1
            for i in index_to_fill[to_fill]:
                for a, b in groups[i]:
                    t += 1
                    flooded.add((a, b))
        print(iterations)
        print(" ".join([str(x) for x in colours[1:]]))

if __name__ == '__main__':
    main()