import sys
l = int(sys.stdin.readline().strip())
d = int(sys.stdin.readline().strip())
x = int(sys.stdin.readline().strip())
numbers = []
for i in range(l, d+1):
    c = 0
    for n in str(i):
        c += int(n)
    if c == x:
        numbers.append(i)

print(numbers[0])
print(numbers[len(numbers)-1])
