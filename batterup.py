n = int(input())
numbers = [int(x) for x in input().split()]
invalid = numbers.count(-1)
print((sum(numbers)+invalid)/(n-invalid))