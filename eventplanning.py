import sys
guidelines = list(map(int, sys.stdin.readline().strip().split()))
budget = guidelines[1]
people = guidelines[0]
hotels = guidelines[2]
options = []
for i in range(0, hotels):
    price_per_night = int(sys.stdin.readline().strip())
    available_rooms = list(map(int, sys.stdin.readline().strip().split()))
    for room in available_rooms:
        if room >= people and budget >= people*price_per_night:
            options.append(people*price_per_night)

if options:
    print(min(options))
else:
    print("stay home")
