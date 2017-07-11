line = list(map(int, input().strip().split()))
while line != [0, 0]:
    head_count, knight_count = line[0], line[1]
    heads, knights = [0]*head_count, [0]*knight_count
    for i in range(0, head_count):
        heads[i] = int(input().strip())
    for i in range(0, knight_count):
        knights[i] = int(input().strip())
    heads = sorted(heads)
    knights = sorted(knights)
    cost, i, j = 0, 0, 0
    while i < head_count and j < knight_count:
        if knights[j] >= heads[i]:
            cost += knights[j]
            i += 1
        j += 1
    if i == head_count:
        print(cost)
    else:
        print("Loowater is doomed!")
    line = list(map(int, input().strip().split()))