n = input()
numbers = list(map(int, input().strip().split()))
numbers = sorted(numbers)
i = 1
a = True
while a and i + 1 < len(numbers):
    if numbers[-i-2] + numbers[-i-1] > numbers[-i]:
        a = False
    i += 1
if not a:
    print("possible")
else:
    print("impossible")
