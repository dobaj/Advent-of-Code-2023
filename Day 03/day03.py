#Part 1
with open("Day 03/input.txt") as f:
    adjacency_map = set()
    i = 0
    sum = 0
    last = None
    line = f.readline()
    while True:
        for j in range(len(line)-1): #trim LF
            if not line[j].isdigit() and line[j] != ".":
                for k in range(-1,2):
                    for l in range(-1,2):
                        adjacency_map.add((i+k,j+l))
        if last:
           isNum, num = False, ""
           for j in range(len(last)): # need extra character to add numbers on the end
            if last[j].isdigit():
                num+=last[j]
                isNum |= (i-1,j) in adjacency_map
            else:
                if isNum:
                    sum+=int(num)
                    isNum = False
                num = ""
        i+=1
        last = line
        if not last:
            break
        line = f.readline()
    print("Part 1:", sum)

#Part 2
with open("Day 3/input.txt") as f:
    star_map = {}
    i = 0
    sum = 0
    last = None
    line = f.readline()
    while True:
        for j in range(len(line)-1): #trim LF
            if line[j] == "*":
                star_map[(i,j)] = []
        if last:
           num = ""
           adjacent_stars = set()
           for j in range(len(last)): # need extra character to add numbers on the end
            if last[j].isdigit():
                num+=last[j]
                for k in range(-1,2):
                    for l in range(-1,2):
                        if (i+k-1,j+l) in star_map:
                            adjacent_stars.add((i+k-1,j+l)) # avoid duplicates
            else:
                for star in adjacent_stars:
                    star_map[star].append(int(num))
                num = ""
                adjacent_stars = set()
        i+=1
        last = line
        if not last:
            break
        line = f.readline()
    for star in star_map:
        if len(star_map[star]) == 2:
            product = 1
            for num in star_map[star]:
                product*=num
            sum += product
    print("Part 2:", sum)