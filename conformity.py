n = int(input().strip())
d = {}
for i in range(0,n):
    line = list(map(int, input().strip().split()))
    line = sorted(line)
    line = list(map(str, line))
    line = " ".join(line)
    if line not in d:
        d[line] = 1
    else: 
        d[line] += 1
numbers = []
for line in d:
    numbers.append(d[line])

numbers = sorted(numbers)
print(numbers[-1]*numbers.count(numbers[-1]))
