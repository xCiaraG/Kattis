from sys import stdin
n = int(stdin.readline())
sentence = stdin.readline().split()
m = int(stdin.readline())
d = {}
for i in range(m):
    word, translation, correct_incorrect = stdin.readline().split()
    if word not in d:
        d[word] = [[0, 0], ""]
    if correct_incorrect == "correct":
        d[word][0][0] += 1
    else:
        d[word][0][1] += 1
    d[word][1] = translation
correct = 1
total = 1
for word in sentence:
    correct *= d[word][0][0]
    total *= sum(d[word][0])

if correct == 1 or total == 1:
    s = ""
    for word in sentence:
        s += d[word][1] + " "
    print(s.strip())
    if correct == 1:
        print("correct")
    else:
        print("incorrect")
else:
    print("{} correct".format(correct))
    print("{} incorrect".format(total - correct))




