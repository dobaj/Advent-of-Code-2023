#Part 1
def dijkstra():
    while True:
        #Get lowest node
        lowest_dist = 0
        lowest_node = None
        for curr in current_pipes:
            if lowest_node == None or pipe_dist[curr[1]][curr[0]] < lowest_dist:
                lowest_dist = pipe_dist[curr[1]][curr[0]]
                lowest_node = curr
        #Remove from pipes to consider
        current_pipes.remove(lowest_node)
        #Get info for this pipe
        x, y = lowest_node
        dx,dy = pipe_dir[y][x]
        shape = pipe_arr[y][x]

        dx, dy = pipes[shape][(dx,dy)]
        newx, newy = x+dx, y+dy
        #If this pipe has already been visited we have cycled through the loop
        if pipe_dist[newy][newx] != float("inf"):
            return(pipe_dist[newy][newx])
        
        current_pipes.add((newx,newy))
        pipe_dist[newy][newx] = pipe_dist[y][x]+1
        pipe_dir[newy][newx] = (dx,dy)

with open("Day 10/input.txt") as f:
    pipe_arr = []
    pipe_dist = []
    pipe_dir = []
    current_pipes = set()
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    
    pipes = {"|": {(0,1): (0,1),(0,-1): (0,-1)}, 
             "-": {(1,0): (1,0),(-1,0): (-1,0)}, 
             "L": {(0,1): (1,0), (-1,0): (0,-1)}, 
             "F": {(0,-1): (1,0), (-1,0): (0,1)}, 
             "J": {(0,1): (-1,0), (1,0): (0,-1)}, 
             "7": {(0,-1): (-1,0), (1,0): (0,1)}}
    
    #Injest pipe map
    for y, line in enumerate(f):
        x = line.find("S")
        pipe_arr.append(line.strip())
        pipe_dist.append([float("inf")]*len(line.strip()))
        pipe_dir.append([(0,0)]*len(line.strip()))
        if x != -1:
            start_x, start_y = x, y
    
    #Start 
    for dy, dx in directions:
        x, y = start_x+dx, start_y+dy
        if y < 0 or y >= len(pipe_arr) or x < 0 or x >= len(pipe_arr[y]):
            continue
        if pipe_arr[y][x] != ".":
            if (dx,dy) in pipes[pipe_arr[y][x]]:
                current_pipes.add((x,y))
                pipe_dist[y][x] = 1
                pipe_dir[y][x] = (dx,dy)
    print("Part 1:", dijkstra())

#Part 2
def dijkstra():
    while True:
        #Get lowest node
        lowest_dist = 0
        lowest_node = None
        for curr in current_pipes:
            if lowest_node == None or pipe_dist[curr[1]][curr[0]] < lowest_dist:
                lowest_dist = pipe_dist[curr[1]][curr[0]]
                lowest_node = curr
        #Remove from current pipes to consider
        current_pipes.remove(lowest_node)
        #Get info for this pipe
        x, y = lowest_node
        dx,dy = pipe_dir[y][x]
        shape = pipe_arr[y][x]

        dx, dy = pipes[shape][(dx,dy)]
        newx, newy = x+dx, y+dy
        #If this pipe has already been visited we have cycled through the loop
        if pipe_dist[newy][newx] != float("inf"):
            return(pipe_dist[newy][newx])
        
        current_pipes.add((newx,newy))
        visited.add((newx,newy))
        pipe_dist[newy][newx] = pipe_dist[y][x]+1
        pipe_dir[newy][newx] = (dx,dy)

def escape(x,y,safe):
    #Can a ground piece reach the outside of the loop
    dot_visit = set()
    nodes = {(x,y)}
    
    while True:
        #If there are no more nodes to explore the piece is inside
        if len(nodes) == 0:
            return False,dot_visit
        add = set()
        #Iterate through all ground pieces, add adjacent
        for node in nodes:
            if node in safe:
                return True, dot_visit
            dot_visit.add(node)
            x,y = node
            for dx,dy in directions:
                if x+dx < 0 or y+dy < 0 or y+dy >= len(pipe_arr) or x+dy >= len(pipe_arr[y+dy]):
                    continue
                if (x+dx,y+dy) not in visited and (x+dx,y+dy) not in dot_visit:
                    add.add((x+dx, y+dy))
        nodes = nodes.difference(dot_visit)
        nodes = nodes.union(add)

with open("Day 10/input.txt") as f:
    pipe_arr = []
    pipe_dist = []
    pipe_dir = []
    current_pipes = set()
    visited = set()
    directions = [(0,-1),(-1,0),(0,1),(1,0)]
    
    pipes = {"|": {(0,1): (0,1),(0,-1): (0,-1)}, 
             "-": {(1,0): (1,0),(-1,0): (-1,0)}, 
             "L": {(0,1): (1,0), (-1,0): (0,-1)}, 
             "F": {(0,-1): (1,0), (-1,0): (0,1)}, 
             "J": {(0,1): (-1,0), (1,0): (0,-1)}, 
             "7": {(0,-1): (-1,0), (1,0): (0,1)}}
    
    #Injest pipe map
    for y, line in enumerate(f):
        x = line.find("S")
        pipe_arr.append(line.strip())
        pipe_dist.append([float("inf")]*len(line.strip()))
        pipe_dir.append([(0,0)]*len(line.strip()))
        if x != -1:
            start_x, start_y = x, y
    
    #Start 
    visited.add((start_x,start_y))
    start_dirs = []
    for dy, dx in directions:
        x, y = start_x+dx, start_y+dy
        if y < 0 or y >= len(pipe_arr) or x < 0 or x >= len(pipe_arr[y]):
            continue
        if pipe_arr[y][x] != ".":
            if (dx,dy) in pipes[pipe_arr[y][x]]:
                start_dirs.append((dx,dy))
                current_pipes.add((x,y))
                visited.add((x,y))
                pipe_dist[y][x] = 1
                pipe_dir[y][x] = (dx,dy)
    
    #Make start piece its own shape
    for key in pipes:
        for value in pipes[key].values():
            if value not in start_dirs:
                break
            start_type = key
    pipe_arr[start_y] = pipe_arr[start_y][:start_x] + start_type + pipe_arr[start_y][start_x+1:]
    dijkstra()
            
    #Find first F then go downwards to go CCW
    for y in range(len(pipe_arr)):
        found_f = False
        for x in range(len(pipe_arr[0])):
            if (x,y) in visited and pipe_arr[y][x] == "F":
                found_f = True
                break
        if found_f:
            break
        
    start_x,start_y = (x,y)
    dx,dy = (0,1)
    ccw_map = {(1,0): (0,1),
                (0,1): (-1,0),
                (-1,0): (0,-1),
                (0,-1): (1,0)}
    safe = set()

    #Go around loop making all pieces on the right side safe
    while True:
        ccw = ccw_map[(dx,dy)]
        #Make piece to the right of our direction safe
        if (x+ccw[0], y+ccw[1]) not in visited:
            safe.add((x+ccw[0], y+ccw[1]))
        #Update to new pipe
        x, y = x+dx, y+dy
        if (x+ccw[0], y+ccw[1]) not in visited:
            safe.add((x+ccw[0], y+ccw[1]))
        #Change direction
        dx, dy = pipes[pipe_arr[y][x]][(dx,dy)]
        if (x,y) == (start_x,start_y):
            break
    
    #Populate safe set
    sum = 0
    for y in range(len(pipe_arr)+1):
        for x in range(len(pipe_arr[0])+1):
            if (x,y) not in safe and (x,y) not in visited:
                esc = escape(x,y,safe)
                if esc[0]:
                    safe = safe.union(escape(x,y,safe)[1])
                else:
                    sum+=1
    print("Part 2:", sum)