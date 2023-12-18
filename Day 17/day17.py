#Part 1
import heapq
cw = [(1,0),(0,1),(-1,0),(0,-1)]

def in_rows(x,y):
    return not (x < 0 or y < 0 or x >= len(rows[0]) or y >= len(rows))

# def get_neighbors(x,y,i,count, dist):
#     neighbors = []
#     dx,dy = cw[i]
#     d=dist
#     c = count
#     l,r = (i-1)%4, (i+1)%4
#     lx,ly = cw[l]
#     rx,ry = cw[r]
#     while c <= 3:
#         if in_rows(x+lx,y+ly):
#             neighbors.append((d+rows[y+ly][x+lx], x+lx,y+ly, l, 1))
#         if in_rows(x+rx,y+ry):
#             neighbors.append((d+rows[y+ry][x+rx], x+rx,y+ry, r, 1))
#         x, y = x+dx, y+dy
#         if not in_rows(x,y):
#             break
#         d += rows[y][x]
#         if c < 3:
#             neighbors.append((d, x, y, i, c+1))
#         c+=1

#     return neighbors

def get_neighbors(x,y,i,count,dist):
    neighbors = []
    dx,dy = cw[i]
    if count != 3:
        #If shorter than maximum we can go forward
        if in_rows(x+dx,y+dy):
            neighbors.append((dist+rows[y+dy][x+dx],x+dx,y+dy,i,count+1))
    #Can always turn
    l,r = (i-1)%4, (i+1)%4
    lx,ly = cw[l]
    rx,ry = cw[r]
    if in_rows(x+lx,y+ly):
        neighbors.append((dist+rows[y+ly][x+lx],x+lx,y+ly, l, 1))
    if in_rows(x+rx,y+ry):
        neighbors.append((dist+rows[y+ry][x+rx],x+rx,y+ry, r, 1))
    return neighbors

def dijkstra(x1, x2):
    # dijkstra using priority queue 
    distance = {}
    Q = []
    for dir in range(4):
        heapq.heappush(Q, (0, *x1, dir, 0))
        distance[(*x1, dir, 0)] = 0

    while Q:
        dist, x, y, low_i, count = heapq.heappop(Q)
        
        for n in get_neighbors(x,y, low_i, count, dist):
            if n[1:] not in distance or n[0] < distance[n[1:]]:
                distance[n[1:]] = n[0]
                heapq.heappush(Q,n)

        if (x,y) == x2:
            return dist

with open("Day 17/input.txt") as f:
    rows = []
    for line in f:
        line=line.strip()
        rows.append(list(map(int,line[::1])))

    first = (0,0)
    last = (len(rows[-1])-1,len(rows)-1)

    print("Part 1:",dijkstra(first,last))


#Part 2
import heapq
cw = [(1,0),(0,1),(-1,0),(0,-1)]

def in_rows(x,y):
    return not (x < 0 or y < 0 or x >= len(rows[0]) or y >= len(rows))

# def get_neighbors(x,y,i,count, dist):
#     #Technically slower but interesting nonetheless
#     neighbors = []
#     dx,dy = cw[i]
#     d=dist
#     c = count
#     if c < 4 and in_rows(x+dx*(4-c),y+dy*(4-c)):
#         while c < 4:
#             x, y = x+dx, y+dy
#             d += rows[y][x]
#             c+=1
#         neighbors.append((d,x,y,i,4))
#     else:
#         return neighbors
#     l,r = (i-1)%4, (i+1)%4
#     lx,ly = cw[l]
#     rx,ry = cw[r]
#     # d = dist
#     while c <= 10:
#         if in_rows(x+lx,y+ly):
#             neighbors.append((d+rows[y+ly][x+lx], x+lx,y+ly, l, 1))
#         if in_rows(x+rx,y+ry):
#             neighbors.append((d+rows[y+ry][x+rx], x+rx, y+ry, r, 1))
#         x, y = x+dx, y+dy
#         if not in_rows(x,y):
#             break
#         d += rows[y][x]
#         if c < 10:
#             neighbors.append((d,x,y,i,c+1))
#         c+=1

#     return neighbors

def get_neighbors(x,y,i,count,dist):
    neighbors = []
    dx,dy = cw[i]
    if count != 10:
        #Cant move forward after 10 moves
        if in_rows(x+dx,y+dy):
            neighbors.append((dist+rows[y+dy][x+dx],x+dx,y+dy,i,count+1))
    if count >= 4:
        #Can only turn after 4 moves
        l,r = (i-1)%4, (i+1)%4
        lx,ly = cw[l]
        rx,ry = cw[r]
        if in_rows(x+lx,y+ly):
            neighbors.append((dist+rows[y+ly][x+lx],x+lx,y+ly, l, 1))
        if in_rows(x+rx,y+ry):
            neighbors.append((dist+rows[y+ry][x+rx],x+rx,y+ry, r, 1))
    return neighbors

def dijkstra(x1, x2):
    # dijkstra using priority queue 
    distance = {}
    Q = []
    for dir in range(4):
        heapq.heappush(Q, (0, *x1, dir, 0))
        distance[(*x1, dir, 0)] = 0

    while Q:
        dist, x, y, low_i, count = heapq.heappop(Q)
        
        for n in get_neighbors(x,y, low_i, count, dist):
            if n[1:] not in distance or n[0] < distance[n[1:]]:
                distance[n[1:]] = n[0]
                heapq.heappush(Q,n)

        if (x,y) == x2:
            return dist



with open("Day 17/input.txt") as f:
    rows = []
    for line in f:
        line=line.strip()
        rows.append(list(map(int,line[::1])))

    first = (0,0)
    last = (len(rows[-1])-1,len(rows)-1)

    print("Part 2:",dijkstra(first,last))