import sys
line = list(map(int, sys.stdin.readline().strip().split()))
n = line[0]
road_length = line[1]
current_time = 0
previous_pos = 0
for i in range(0, n):
    line = list(map(int, sys.stdin.readline().strip().split()))
    current_time += line[0] - previous_pos
    total_light_time = line[1] + line[2]
    current_pos = current_time % total_light_time
    if current_pos < line[1]:
        current_time += line[1] - current_pos
    previous_pos = line[0]

print(current_time + road_length - previous_pos)
