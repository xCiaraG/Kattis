import sys
want = [1, 1, 2, 2, 2, 8]
get = []
have = list(map(int, sys.stdin.readline().strip().split()))
i = 0
while i < len(want):
    get.append(want[i] - have[i])
    i += 1
get = list(map(str, get))
print(" ".join(get))
