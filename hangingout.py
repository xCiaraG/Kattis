capacity, events = [int(x) for x in input().split()]
current = 0
denied = 0
for _ in range(events):
	event = input().split()
	if event[0] == "leave":
		current -= int(event[1])
	elif current + int(event[1]) > capacity:
		denied += 1
	else:
		current += int(event[1])
print(denied)