n = int(input())
seeds = list(map(int, input().strip().split()))
m = 0
i = 0
seeds = sorted(seeds)
seeds.reverse()
while i < len(seeds):
    if seeds[i] + i + 2 > m:
        m = seeds[i] + i + 2
    i += 1
print(m)
