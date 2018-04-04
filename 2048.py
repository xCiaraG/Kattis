import sys
def move_left(numbers):
    n = []
    new_numbers = []
    for number in numbers:
        if number != 0:
            n.append(number)
    i = 0
    while i < len(n):
        if i < len(n)-1 and n[i] == n[i+1]:
            new_numbers.append(n[i]*2)
            i += 2
        else:
            new_numbers.append(n[i])
            i += 1
    while len(new_numbers) != 4:
        new_numbers.append(0)
    return new_numbers

def move_right(numbers):
    numbers.reverse()
    n = []
    new_numbers = []
    for number in numbers:
        if number != 0:
            n.append(number)
    i = 0
    while i < len(n):
        if i < len(n)-1 and n[i] == n[i+1]:
            new_numbers.append(n[i]*2)
            i += 2
        else:
            new_numbers.append(n[i])
            i += 1
    while len(new_numbers) != 4:
        new_numbers.append(0)
    new_numbers.reverse()
    return new_numbers

def shift(numbers):
    new_numbers = [[],[],[],[]]
    i = len(numbers[0]) -1
    k = 0
    while i != -1:
        j = 0
        while j < len(numbers):
            new_numbers[k].append(numbers[j][i])
            j += 1
        k += 1
        i -= 1
    return new_numbers

numbers = []
i = 0
while i < 4:
    numbers.append(list(map(int, sys.stdin.readline().strip().split())))
    i += 1

new_numbers = []
direction = sys.stdin.readline().strip()
if direction == "0":
    for line in numbers:
        new_numbers.append(move_left(line))
elif direction == "2":
    for line in numbers:
        new_numbers.append(move_right(line))
elif direction == "1":
    numbers = shift(numbers)
    for line in numbers:
        new_numbers.append(move_left(line))
    new_numbers = shift(new_numbers)
    new_numbers = shift(new_numbers)
    new_numbers = shift(new_numbers)
else:
    numbers = shift(numbers)
    for line in numbers:
        new_numbers.append(move_right(line))
    new_numbers = shift(new_numbers)
    new_numbers = shift(new_numbers)
    new_numbers = shift(new_numbers)

for line in new_numbers:
    line = list(map(str, line))
    print(" ".join(line))
    