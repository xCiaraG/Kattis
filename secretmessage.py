n = int(input().strip())
for i in range(0, n):
    message = input().strip()
    length = len(message)
    i = 1
    while i**2 < length:
        i += 1
    tmp = "*"*((i**2)-length)
    message += tmp
    new_message = []
    for j in range(0, i):
        tmp = []
        for k in range(0, i):
            tmp.append(message[(j*i)+k])
        new_message.append(tmp)
    new_s = ""
    j = 0
    while j < i:
        k = i - 1
        while k != -1:
            if new_message[k][j] != "*":
                new_s += new_message[k][j]
            k -= 1
        j += 1
    print(new_s)
