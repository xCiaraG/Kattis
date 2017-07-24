score = int(input())
if score > 180 or score in [179, 178, 176, 175, 173, 172, 170, 169, 167, 
                            166, 164, 163, 161, 155, 149, 143]:
    print("impossible")
    score = 0
elif score == 145:
    print("triple", 20)
    print("triple", 15)
    print("double", 20)
    score = 0
elif score == 151:
    print("triple", 20)
    print("triple", 17)
    print("double", 20)
    score = 0
elif score == 157:
    print("triple", 20)
    print("triple", 19)
    print("double", 20)
    score = 0
count = 0
while score != 0:
    i = 20
    while i != 0:
        if score - i*3 >= 0:
            print("triple", i)
            score = score - i*3
            count += 1
            break
        elif score - i*2 >= 0 and (count < 2 or score <= 40 and score - i*2 == 0):
            print("double", i)
            score = score - i*2
            count += 1
            break
        elif score - i >= 0 and (count < 2 or score <= 20 and score - i == 0):
            print("single", i)
            score -= i
            count += 1
            break
        i -= 1
