import datetime
d = list(map(int, input().strip().split()))
days = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
day = datetime.date(2009, d[1], d[0]).weekday()
print(days[day])
