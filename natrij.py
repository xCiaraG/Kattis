from datetime import datetime, timedelta
t1 = input()
t2 = input()
tdelta = datetime.strptime(t2, '%H:%M:%S') - datetime.strptime(t1, '%H:%M:%S')
if tdelta.days < 0:
    tdelta = timedelta(days=0, seconds=tdelta.seconds, microseconds=tdelta.microseconds)
s = str(tdelta)
if s == "0:00:00":
	s = "24:00:00"
if len(s) == 7:
	print("0"+ s)
else:
	print(s)