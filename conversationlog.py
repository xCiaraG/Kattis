nt(input().strip())
d = {}
d_count = {}
for i in range(0, n):
    line = input().strip().split()
    if line[0] not in d:
        d[line[0]] = (" ".join(line[1:]))
    else:
        d[line[0]] += " " + " ".join(line[1:])

    for word in line[1:]:
        if word not in d_count:
            d_count[word] = 1
        else:
            d_count[word] += 1
new = []
for key in d:
    d[key] = d[key].split()
    new.append(set(d[key]))

s = new[0]
for se in new[1:]:
    s = s.intersection(se)

counts = []
for word in s:
    counts.append((d_count[word], word))
if counts:
    counts = sorted(counts)
    counts = counts[::-1]
    i = 0
    while i < len(counts):
        to_sort = []
        to_sort.append(counts[i][1])
        j = i + 1
        while j < len(counts) and counts[i][0] == counts[j][0]:
            to_sort.append(counts[j][1])
            j += 1
        to_sort = sorted(to_sort)
        for word in to_sort:
            print(word)
        i = j
else:
    print("ALL CLEAR")
