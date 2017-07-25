from sys import stdin

jack_jill = [int(x) for x in raw_input().split()]

while jack_jill != [0,0]:

    count = 0
    jack_num = jack_jill[0]
    jill_num = jack_jill[1]
    jack = [0]*jack_num

    for i in range(0, jack_num):
        jack[i] = int(stdin.readline())
    i = 0
    for j in range(0, jill_num):
        tmp = int(stdin.readline())
        while i < jack_num and jack[i] < tmp:
        	i += 1
        if i < jack_num and jack[i] == tmp:
        	count += 1
    print(count)

    jack_jill = [int(x) for x in raw_input().split()]