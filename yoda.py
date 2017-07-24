number1 = input()
number2 = input()
while len(number1) < len(number2):
    number1 = "0" + number1
while len(number2) < len(number1):
    number2 = "0" + number2

new_number1 = ""
new_number2 = ""

i = 0
while i < len(number1):
    if int(number1[i]) > int(number2[i]):
        new_number1 += number1[i]
    elif int(number1[i]) < int(number2[i]):
        new_number2 += number2[i]
    else:
        new_number1 += number1[i]
        new_number2 += number2[i]
    i += 1

if new_number1:
    print(int(new_number1))
else:
    print("YODA")

if new_number2:
    print(int(new_number2))
else:
    print("YODA")
