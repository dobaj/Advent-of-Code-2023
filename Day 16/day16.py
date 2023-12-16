# Part 1
def traverse(x,y,dir_i):
    # Iteratively traverse beams
    # Discards beam if it matches a previous beam
    past_beams = set()
    display = set()
    beams = set([(x,y,dir_i)])
    while beams:
        new_b = set()
        for b in beams:
            x,y,dir_i = b
            if (x,y,dir_i) in past_beams or x >= len(rows[0]) or \
                y >= len(rows) or x < 0 or y < 0:
                continue
            display.add((x,y)) # Avoid duplicates
            past_beams.add((x,y, dir_i))
            shape = rows[y][x]
            if shape == ".":
                dx,dy = cw_dirs[dir_i]
                new_b.add((x+dx,y+dy,dir_i))
                continue
            next_dirs = shapes[shape][dir_i]
            for d in next_dirs:
                # In case the beam splits
                dx,dy = cw_dirs[d]
                new_b.add((x+dx,y+dy,d))
        beams = new_b
    return len(display)

with open("Day 16/input.txt") as f:
    # Define shape behaviour and directions
    cw_dirs = [(1,0),(0,1),(-1,0),(0,-1)]
    shapes = {"/": {0:[3], 1:[2], 2:[1], 3:[0]}, "\\": {0:[1], 3:[2], 2:[3], 1:[0]}, "|": {0: [1, 3], 2: [1,3], 3: [3], 1: [1]}, "-": {0: [0], 1: [0,2], 2: [2], 3: [0,2]}}
    rows = [x.strip() for x in f]
    x, y, dir_i = 0,0,0

    print("Part 1:", traverse(x,y,dir_i))

# Part 2
def traverse(x,y,dir_i):
    # Iteratively traverse beams
    # Discards beam if it matches a previous beam
    past_beams = set()
    display = set()
    beams = set([(x,y,dir_i)])
    while beams:
        new_b = set()
        for b in beams:
            x,y,dir_i = b
            if (x,y,dir_i) in past_beams or x >= len(rows[0]) or \
                y >= len(rows) or x < 0 or y < 0:
                continue
            display.add((x,y)) # Avoid duplicates
            past_beams.add((x,y, dir_i))
            shape = rows[y][x]
            if shape == ".":
                dx,dy = cw_dirs[dir_i]
                new_b.add((x+dx,y+dy,dir_i))
                continue
            next_dirs = shapes[shape][dir_i]
            for d in next_dirs:
                # In case the beam splits
                dx,dy = cw_dirs[d]
                new_b.add((x+dx,y+dy,d))
        beams = new_b
    return len(display)

with open("Day 16/input.txt") as f:
    # Define shape behaviour and directions
    cw_dirs = [(1,0),(0,1),(-1,0),(0,-1)]
    shapes = {"/": {0:[3], 1:[2], 2:[1], 3:[0]}, "\\": {0:[1], 3:[2], 2:[3], 1:[0]}, "|": {0: [1, 3], 2: [1,3], 3: [3], 1: [1]}, "-": {0: [0], 1: [0,2], 2: [2], 3: [0,2]}}
    rows = [x.strip() for x in f]

    max_e = 0
    for y in range(len(rows)):
        # Approach from both vertical edges
        max_e = max(traverse(0,y,0),max_e)
        max_e = max(traverse(len(rows[y])-1,y,2),max_e)
    for x in range(len(rows[0])):
        # Approach from both horizontal edges
        max_e = max(traverse(x,0,1),max_e)
        max_e = max(traverse(x,len(rows)-1,3),max_e)
    print("Part 2:", max_e)