import re
# Part 1
with open("Day 11/input.txt") as f:
    galaxies = {}
    image = []
    galaxy_num = 1 # used for naming galaxies

    offset = 0
    for y, line in enumerate(f):
        find = list(re.finditer("#",line))
        if not find:
            #add extra row
            offset+=1
        for galaxy in find:
            m = galaxy.start() # index of galaxy
            galaxies[galaxy_num] = (m,y+offset)
            galaxy_num+=1
        # using image to add col based offset
        image.append(line)  
    
    #add column offsets using image
    i = 0
    offset = 0
    while i < len(image[0]):
        empty = True
        for l in image:
            if l[i] != ".":
                empty = False
                break
        if empty:
            #add extra column to all galaxies after this column
            for galaxy in galaxies:
                coords = galaxies[galaxy]
                if coords[0] > i+offset:
                    galaxies[galaxy] = coords[0]+1, coords[1]
            offset+=1
        i+=1

    pairs = {}
    
    for galaxy in galaxies:
        for other in galaxies:
            if galaxy != other and (galaxy,other) not in pairs and (other,galaxy) not in pairs:
                x0, y0 = galaxies[galaxy]
                x1, y1 = galaxies[other]
                pairs[(galaxy,other)] = abs(y0-y1) + abs(x0-x1)
    
    sum = 0
    for pair in pairs:
        sum += pairs[pair]

    print("Part 1:", sum)

import re
# Part 2
with open("Day 11/input.txt") as f:
    galaxies = {}
    image = []
    galaxy_num = 1 # used for naming galaxies
    empty_size = 1000000

    offset = 0
    for y, line in enumerate(f):
        find = list(re.finditer("#",line))
        if not find:
            #add extra rows
            offset+=empty_size-1
        for galaxy in find:
            m = galaxy.start() # index of galaxy
            galaxies[galaxy_num] = (m,y+offset)
            galaxy_num+=1
        image.append(line)  
    
    #add column offsets using image
    i = 0
    offset = 0
    while i < len(image[0]):
        empty = True
        for l in image:
            if l[i] != ".":
                empty = False
                break
        if empty:
            #add extra column to all galaxies after this column
            for galaxy in galaxies:
                coords = galaxies[galaxy]
                if coords[0] > i + offset:
                    galaxies[galaxy] = coords[0]+empty_size-1, coords[1]
            offset+=empty_size-1
        i+=1

    pairs = {}
    
    for galaxy in galaxies:
        for other in galaxies:
            if galaxy != other and (galaxy,other) not in pairs and (other,galaxy) not in pairs:
                x0, y0 = galaxies[galaxy]
                x1, y1 = galaxies[other]
                pairs[(galaxy,other)] = abs(y0-y1) + abs(x0-x1)
    
    sum = 0
    for pair in pairs:
        sum += pairs[pair]

    print("Part 2:", sum)