numbers = input().strip().split()
n1 = numbers[0][::-1]
n2 = numbers[1][::-1]
if n1 > n2:
    print(n1)
else:
    print(n2)
