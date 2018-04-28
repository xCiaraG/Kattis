from sys import stdin
from collections import defaultdict

def main():
    n, m = [int(x) for x in stdin.readline().split()]
    teams_solved = defaultdict(set)
    solved = [0]*(n + 1)
    penalty = [0]*(n + 1)
    current_pos = 1
    for _ in range(m):
        t, p = [int(x) for x in stdin.readline().split()]
        solved[t] += 1
        teams_solved[solved[t]].add(t)
        if solved[t] != 1:
            teams_solved[solved[t] - 1].remove(t)
        penalty[t] += p
        if t == 1:
            for team in teams_solved[solved[t]]:
                if penalty[1] <= penalty[team] and team != 1:
                    current_pos -= 1 
            for team in teams_solved[solved[t] - 1]:
                if penalty[1] - p > penalty[team]:
                    current_pos -= 1
        elif solved[t] == solved[1] and penalty[t] < penalty[1]:
            current_pos += 1
        elif solved[t] == solved[1] + 1 and penalty[1] <= (penalty[t] - p):
            current_pos += 1
        print(current_pos)

if __name__ == '__main__':
    main()