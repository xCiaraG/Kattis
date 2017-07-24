import sys
n = int(sys.stdin.readline().strip())
for i in range(0, n):
    numbers = []
    m = int(sys.stdin.readline().strip())
    for j in range(0, m):
        numbers.append(sys.stdin.readline().strip())
    numbers = sorted(numbers)
    k = 0
    a = True
    while k < len(numbers) - 1:
        if len(numbers[k]) <= len(numbers[k+1]):
            if numbers[k] == numbers[k+1][:len(numbers[k])]:
                a = False
                k = len(numbers) + 1
        k += 1
    if a:
        print("YES")
    else:
        print("NO")
