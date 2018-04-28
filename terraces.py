from sys import stdin
from collections import deque

def main():
    m, n = [int(x) for x in stdin.readline().split()]
    land = []
    for _ in range(n):
        land.append([int(x) for x in stdin.readline().split()])

    total = 0
    seen = [[True for _ in range(m)] for _ in range(n)]

    for tmpi in range(n):
        for tmpj in range(m):
            lower = True
            i, j = tmpi, tmpj
            if seen[i][j]:
                num = land[i][j]
                lower = False
                current = 0
                seen[i][j] = False
                to_check = deque([(i, j)])
                while to_check:
                    current += 1
                    i, j = to_check.popleft()
                    for i, j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        if 0 <= i < n and 0 <= j < m:
                            if land[i][j] == num and seen[i][j]:
                                seen[i][j] = False
                                to_check.append((i, j))
                            elif land[i][j] < num:
                                lower = True
            if not lower:
                total += current
    print(total)

if __name__ == '__main__':
    main()