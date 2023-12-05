import re

# Part 1
def ingest_map(farm_map):
    for _ in range(2):
        line = f.readline()
    while line.strip():
        dest, start, map_range = map(int,re.findall("[0-9]+", line))
        farm_map[start] = (map_range, dest)
        line = f.readline()

def get_dest(farm_map, source):
    for m in farm_map:
        if source < m:
            continue
        diff = source - m
        if diff < farm_map[m][0]:
            return farm_map[m][1] + diff
    return source

with open("Day 5/input.txt") as f:
    line = f.readline()
    seeds = re.findall("[0-9]+",line)
    seeds = list(map(int, seeds))
    line = f.readline()
    
    mapmap ={"seed_soil": {},
    "soil_fert": {},
    "fert_water": {},
    "water_light": {},
    "light_temp": {},
    "temp_humid": {},
    "humid_loc": {}}
    for m in mapmap:
        ingest_map(mapmap[m])
    
    locations = []
    for seed in seeds:
        for m in mapmap:
            seed = get_dest(mapmap[m], seed)
        locations.append(seed)
    
    locations.sort()
    print("Part 1:",locations[0])

# Part 2
def ingest_map(farm_map):
    for _ in range(2):
        line = f.readline()
    while line.strip():
        dest, start, map_range = map(int,re.findall("[0-9]+", line))
        farm_map[start] = (map_range, dest)
        line = f.readline()

def get_dest(farm_map: dict, source, input_range):
    dest_ranges = []
    last_map_max = 0
    keys = list(farm_map.keys())
    keys.sort()
    for m in keys:
        if input_range <= 0:
            break
        if source > m + farm_map[m][0]:
            continue
        start = source - m # Amount inside bucket (or outside bucket)
        if source < m and source > last_map_max: # If in between buckets
            input_range = source + input_range - m
            dest_ranges.append((source, -start))
            source = m
            continue
        location_range = min(farm_map[m][0]-start,input_range)
        dest_ranges.append((farm_map[m][1]+start,location_range))
        if input_range >= location_range:
            source += location_range
            input_range -= location_range
        last_map_max = m + farm_map[m][0]
    # Fill remaining range
    if input_range > 0:
        dest_ranges.append((source, input_range))
    return dest_ranges

with open("Day 5/input.txt") as f:
    line = f.readline()
    seeds = re.findall("[0-9]+",line)
    seeds = list(map(int, seeds))
    line = f.readline()
    
    mapmap ={"seed_soil": {},
    "soil_fert": {},
    "fert_water": {},
    "water_light": {},
    "light_temp": {},
    "temp_humid": {},
    "humid_loc": {}
    }
    for m in mapmap:
        ingest_map(mapmap[m])
    
    minimum = float("inf")
    for i in range(0, len(seeds)//2, 2):
        in_arr = [(seeds[i],seeds[i+1])]
        for m in mapmap:
            out = []
            for seed, seed_range in in_arr:
                out += get_dest(mapmap[m], seed, seed_range)
            in_arr = out
        for i in out:
            minimum = min(i[0],minimum)

    print("Part 2:",minimum)