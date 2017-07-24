numbers = list(map(int, input().strip().split()))
while numbers != sorted(numbers):
    i = 0
    while i < len(numbers) - 1:
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            numbers = list(map(str, numbers))
            print(" ".join(numbers))
            numbers = list(map(int, numbers))
        i += 1
