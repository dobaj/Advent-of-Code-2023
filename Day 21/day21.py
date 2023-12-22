#Part 1
with open("Day 21/input.txt") as f:
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]
    steps = 64
    rows = []
    nodes = set()

    for i, line in enumerate(f):
        line = line.strip()
        if "S" in line:
            s = line.find("S")
            nodes.add((i,s))
            line = line[:s] + "." + line[s+1:]
        rows.append(line)
        
    i = 0
    while i < steps:
        new_nodes = set()
        for x, y in nodes:
            for dx,dy in dirs:
                if y+dy >= 0 and y+dy < len(rows) and x+dx >= 0 and x+dx < len(rows[y]):
                    if rows[y+dy][x+dx] == ".":
                        new_nodes.add((x+dx,y+dy))
        nodes=new_nodes
        i+=1
    
    print("Part 1:", len(nodes))

#Part 2
import numpy as np

def check(nodes, move_count):
    i = 0
    while i < move_count:
        new_nodes = set()
        for x, y in nodes:
            for dx,dy in dirs:
                    if rows[(y+dy) % len(rows)][(x+dx) % len(rows[0])] == ".":
                        new_nodes.add((x+dx,y+dy))
        nodes=new_nodes
        i+=1
    return nodes

with open("Day 21/input.txt") as f:
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]
    steps = 26501365
    rows = []
    nodes = set()

    for i, line in enumerate(f):
        line = line.strip()
        if "S" in line:
            s = line.find("S")
            nodes.add((i,s))
            line = line[:s] + "." + line[s+1:]
        rows.append(line)
        
    x, y = [], []
    past = 0

    #Get first 3 occurences
    for i in range(0,3):
        j = steps%len(rows) + i*len(rows)
        x.append(j)
        nodes = check(nodes,j-past)
        y.append(len(nodes))
        past = j
    
    #Fit quadratic
    z = np.polyfit(x,y,2)
    z = int(z[0]*steps**2 + z[1]*steps + z[2])
    print("Part 2:", z)