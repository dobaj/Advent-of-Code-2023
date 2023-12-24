#Part 1
def in_range(x,y):
    return x >= 0 and y >= 0 and y < len(rows) and x < len(rows[y])

def find_longest(start, end, visited = []):
    #BFS because recursion depth is too high
    longest = 0
    nodes = set()
    nodes.add((start,()))
    while nodes:
        remove = set()
        add = set()
        for node in nodes:
            remove.add(node)
            start, visited = node

            if start == end:
                longest = max(longest, len(visited))
                continue

            for dx, dy in dirs:
                new_visited = list(visited)
                x,y = start[0]+dx, start[1]+dy
                if (x,y) in new_visited or not in_range(x,y) or rows[y][x] == "#":
                    continue
                shape = rows[y][x]
                if shape == ">" or shape == "<" or shape == "^" or shape == "v":
                    #Add node to visited to get proper length
                    new_visited.append((x,y))
                    if shape == ">":
                        x,y = x+1,y
                    elif shape == "<":
                        x,y = x-1,y
                    elif shape == "v":
                        x,y = x,y+1
                    elif shape == "^":
                        x,y = x,y-1
                    if (x,y) in new_visited or not in_range(x,y) or rows[y][x] == "#":
                        continue
                new_visited.append((x,y))
                add.add(((x,y),tuple(new_visited)))
        nodes = nodes.difference(remove)
        nodes = nodes.union(add)
    return longest


with open("Day 23/input.txt") as f:
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]
    rows = []
    start, end = 0, 0
    for i, line in enumerate(f):
        line = line.strip()
        if len(line.replace("#","")) == 1:
            if not start:
                start = (line.find("."), i)
            else:
                end = (line.find("."), i)
        rows.append(line)

    print("Part 1:",find_longest(start,end))

#Part 2
def in_range(x,y):
    return x >= 0 and y >= 0 and y < len(rows) and x < len(rows[y])

def get_neigh(x,y):
    neigh = {}
    for dx, dy in dirs:
        newx,newy = x+dx, y+dy
        if not in_range(newx,newy) or rows[newy][newx] == "#":
            continue
        neigh[(newx,newy)] = 1
    neighbours[(x,y)] = neigh

def find_longest(start, end, visited = set(), length = 0):
    if start == end:
        return length
    longest = 0
    for neigh in neighbours[start]:
        if neigh in visited:
            continue
        new = visited.copy()
        new.add(neigh)
        longest = max(longest,find_longest(neigh,end,new,length + neighbours[start][neigh]))
    return longest


with open("Day 23/input.txt") as f:
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]
    rows = []
    start, end = 0, 0
    neighbours = {}
    for i, line in enumerate(f):
        line = line.strip()
        if len(line.replace("#","")) == 1:
            if not start:
                start = (line.find("."), i)
            else:
                end = (line.find("."), i)
        rows.append(line)

    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if rows[i][j] != "#":
                #Get a map of node to neighbours
                get_neigh(j,i)

    remove = set()
    for n in neighbours:
        if len(neighbours[n]) == 2:
            #Can condense if there are two neighbours
            m, l = neighbours[n]
            edge_weight = neighbours[n][m] + neighbours[n][l]
            neighbours[m].pop(n)
            neighbours[m][l] = edge_weight
            neighbours[l].pop(n)
            neighbours[l][m] = edge_weight
            remove.add(n)
    for r in remove:
        neighbours.pop(r)

    print("Part 2:",find_longest(start,end))