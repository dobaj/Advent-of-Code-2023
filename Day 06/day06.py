import re
import math

# Part 1
with open("Day 06/input.txt") as f:
    times = re.findall("[0-9]+", f.readline())
    records = re.findall("[0-9]+", f.readline())
    product = 1
    for i in range(len(times)):
        race_time = int(times[i])
        distance = int(records[i])
        # Follows quadratic formula where b is speed, a is -1, c is dist, 
        # can simplify out negative by swapping min and max
        min_time_held = (-race_time - math.sqrt(race_time*race_time-4*distance))//2 
        max_time_held = (-race_time + math.sqrt(race_time*race_time-4*distance))//2
        product *= int(max_time_held-min_time_held)
    print("Part 1:", product)

# Part 2
with open("Day 06/input.txt") as f:
    times = re.search("[0-9]+", f.readline().replace(" ","")).group(0)
    records = re.search("[0-9]+", f.readline().replace(" ","")).group(0)
    race_time = int(times)
    distance = int(records)
    # Follows quadratic formula where b is speed, a is -1, c is dist, 
    # can simplify out negative by swapping min and max
    min_time_held = (-race_time - math.sqrt(race_time*race_time-4*distance))//2 
    max_time_held = (-race_time + math.sqrt(race_time*race_time-4*distance))//2
    print("Part 2:", int(max_time_held-min_time_held))