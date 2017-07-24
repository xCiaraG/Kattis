dog_times = list(map(int, input().strip().split()))
times = list(map(int, input().strip().split()))

for t in times:
    if dog_times[0] >= t % (dog_times[0] + dog_times[1]) > 0 and dog_times[2] >= t % (dog_times[2] + dog_times[3]) > 0:
        print("both")
    elif dog_times[0] >= t % (dog_times[0] + dog_times[1]) > 0 or dog_times[2] >= t % (dog_times[2] + dog_times[3]) > 0:
        print("one")
    else:
        print("none")
