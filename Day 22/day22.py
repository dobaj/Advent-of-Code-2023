#Part 1
def round(j):
    #Clip to -1 0 and 1
    if j >= 1:
        return 1
    if j <= -1:
        return -1
    return 0

def iterate(start,end):
    #Adds all cubes that form brick to an arr
    x1, y1, z1 = start
    x2, y2, z2 = end
    dx, dy, dz = round(x2-x1), round(y2-y1), round(z2-z1)
    arr = []
    while (x1,y1,z1) != (x2,y2,z2):
        arr.append((x1,y1,z1))
        x1,y1,z1 = x1+dx,y1+dy,z1+dz
    arr.append((x1,y1,z1))
    return arr

def drop(name, start,end):
    start,end = start,end
    while(True):
        it = iterate(start,end)
        for x in it:
            if (x[0],x[1],x[2]-1) in bricks and bricks[(x[0],x[1],x[2]-1)] != name:
                #We have reached the minimum possible height
                return name, start, end
        if it[0][2] > 1:
            for x in it:
                bricks.pop(x)
                bricks[(x[0],x[1],x[2]-1)] = name
            start = (start[0],start[1],start[2]-1)
            end = (end[0],end[1],end[2]-1)
        else:
            #We are at the bottom
            return name, start, end
        
def supported(name,start,end):
    #Checks what bricks support this one
    supp_by = []
    for x in iterate(start,end):
        below = (x[0],x[1],x[2]-1)
        if below in bricks and bricks[below] != name:
                if bricks[below] not in supp_by:
                    supp_by.append(bricks[below])
    held_by[name] = (supp_by)

with open("Day 22/input.txt") as f:
    bricks = {} #Each cube and what brick they belong to
    brick_arr = [] #start and end coords for each brick
    held_by = {} #What bricks are holding this brick

    name = 0
    for line in f:
        line = line.strip().split("~")
        start = tuple(map(int,line[0].split(",")))
        end = tuple(map(int,line[1].split(",")))
        arr = (iterate(start,end))

        brick_arr.append(((name),start,end))
        for c in arr:
            bricks[c] = (name)
        name+=1
    
    #Sort in ascending order
    brick_arr.sort(key=lambda a: a[1][2])
    for name in range(len(brick_arr)):
        brick = brick_arr[name]
        brick_arr[name] = drop(*brick)
    for name, start, end in brick_arr:
        supported(name,start, end)

    removed = set()
    for name, start, end in brick_arr:
        removed.add(name)
        if len(held_by[name]) <= 1:
            for x in held_by[name]:
                if x in removed:
                    removed.remove(x)
    
    print("Part 1:",len(removed))


#Part 2
def round(j):
    #Clip to -1 0 and 1
    if j >= 1:
        return 1
    if j <= -1:
        return -1
    return 0

def iterate(start,end):
    #Adds all cubes that form brick to an arr
    x1, y1, z1 = start
    x2, y2, z2 = end
    dx, dy, dz = round(x2-x1), round(y2-y1), round(z2-z1)
    arr = []
    while (x1,y1,z1) != (x2,y2,z2):
        arr.append((x1,y1,z1))
        x1,y1,z1 = x1+dx,y1+dy,z1+dz
    arr.append((x1,y1,z1))
    return arr

def drop(name, start,end):
    start,end = start,end
    while(True):
        it = iterate(start,end)
        for x in it:
            if (x[0],x[1],x[2]-1) in bricks and bricks[(x[0],x[1],x[2]-1)] != name:
                #We have reached the minimum possible height
                return name, start, end
        if it[0][2] > 1:
            for x in it:
                bricks.pop(x)
                bricks[(x[0],x[1],x[2]-1)] = name
            start = (start[0],start[1],start[2]-1)
            end = (end[0],end[1],end[2]-1)
        else:
            #We are at the bottom
            return name, start, end
        
def supported(name,start,end):
    #Checks what bricks support this one
    supp_by = []
    for x in iterate(start,end):
        below = (x[0],x[1],x[2]-1)
        if below in bricks and bricks[below] != name:
                if bricks[below] not in supp_by:
                    supp_by.append(bricks[below])
    held_by[name] = (supp_by)

with open("Day 22/input.txt") as f:
    bricks = {} #Each cube and what brick they belong to
    brick_arr = [] #start and end coords for each brick
    held_by = {} #What bricks are holding this brick
    
    name = 0
    for line in f:
        line=line.strip().split("~")
        start = tuple(map(int,line[0].split(",")))
        end = tuple(map(int,line[1].split(",")))
        arr = (iterate(start,end))

        brick_arr.append(((name),start,end))
        for c in arr:
            bricks[c] = (name)
        name+=1

    #Sort in ascending order
    brick_arr.sort(key=lambda a: (a[1][2]))
    for name in range(len(brick_arr)):
        brick = brick_arr[name]
        brick_arr[name] = drop(*brick)
    for name, start, end in brick_arr:
        supported(name,start, end)
    

    sum_of = 0
    for i in range(len(brick_arr)):
        i_brick = brick_arr[i][0]
        fall = set()
        fall.add(i_brick)
        for j in range(i+1,len(brick_arr)):
            j_brick = brick_arr[j][0]
            if len(held_by[j_brick]) != 0:
                #If the brick isnt held by anything its at the bottom
                fall.add(j_brick)
                for x in held_by[j_brick]:
                    if x not in fall:
                        fall.remove(j_brick)    
                        break
        fall.remove(i_brick)
        sum_of += len(fall)
    
    print("Part 2:",sum_of)