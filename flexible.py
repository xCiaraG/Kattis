line = list(map(int, input().strip().split()))
partitions = [0] + list(map(int, input().strip().split())) + [line[0]]
sizes = []
i = 0
while i < len(partitions):
    j = i + 1
    while j < len(partitions):
        sizes.append(partitions[j] - partitions[i])
        j += 1
    i += 1
sizes = sorted(set(sizes))
print(*sizes)