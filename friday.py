n = int(input())
for i in range(n):
    days = list(map(int, input().strip().split()))
    months = list(map(int, input().strip().split()))
    fridays = 0
    day = 1
    j = 0
    for month in months:
        if day == 1 and month >= 13:
            fridays += 1
        day = (((month % 7) + day))
        if day > 7:
            day = day % 7  
    print(fridays)
