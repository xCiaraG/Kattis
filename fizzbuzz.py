import sys
n = list(map(int, sys.stdin.readline().strip().split()))
for i in range(1, n[2] + 1):
    if i % n[0] == 0 and i % n[1] == 0:
        print("FizzBuzz")
    elif i % n[0] == 0:
        print("Fizz")
    elif i % n[1] == 0:
        print("Buzz")
    else:
        print(i)
