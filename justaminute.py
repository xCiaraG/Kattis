n = int(input())
total_minutes = 0
total_actual = 0
for i in range(0, n):
    time = list(map(float, input().strip().split()))
    total_minutes += time[0]*60
    total_actual += time[1]

average = total_actual/total_minutes
if average <= 1:
    print("measurement error")
else:
    print("{:.9f}".format(average))
