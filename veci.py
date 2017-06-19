def find_next_highest(num):
    prev = num[-1]
    i = len(num) - 2
    while i > 0 and num[i] >= prev:
        prev = num[i]
        i -= 1
    last = num[i]
    if i + 1 < len(num):
        tmp = num[i+1:]
    tmp = sorted(tmp)
    j = 0
    while tmp[j] <= last:
        j += 1
    prev = tmp[j]
    tmp[j] = last
    num = num[:i] + prev + "".join(sorted(list(tmp)))
    return num

num = input().strip()
if list(num) == sorted(num, reverse=True):
    print("0")
else:
    tmp = find_next_highest(num)
    print(tmp)