import re
import numpy as np 

def dig(x,y,i,arr):
    amt = directions[i][1]
    direct = directions[i][0]
    dx, dy = dirs[direct]
    curr = direct
    next = directions[(i+1)%len(directions)][0]

    x, y = x+dx*(amt), y+dy*(amt)
    curr = "".join(sorted([curr,next]))
    #Change coords based on what type of corner it is
    if curr == "DR":
        arr.append(x+1)
        arr.append(y)
    elif curr == "DL":
        arr.append(x+1)
        arr.append(y+1)
    elif curr == "LU":
        arr.append(x)
        arr.append(y+1)
    else:
        arr.append(x)
        arr.append(y)
    return x, y

with open("Day 18/input.txt") as f:
    dirs = {"R": (1,0), "D": (0,1), "L": (-1,0), "U": (0,-1)}
    trench = {}
    arr = []

    directions = []
    for line in f:
        direction = (re.search("[RDLU]", line).group(0))
        amount = (int(re.search("[0-9]+", line).group(0)))
        directions.append((direction,amount))
        
    x,y = 0,0
    for i in range(len(directions)):
        x,y = dig(x,y,i,arr)
    
    #Use gauss's area formula
    arr = np.reshape(arr,(-1,2))
    x = (arr[:,0])
    y = (arr[:,1])
    
    s1 = np.sum(x*np.roll(y,-1))
    s2 = np.sum(y*np.roll(x,-1))
    total = int(0.5*abs(s1-s2))

    print("Part 1:", total)


#Part 2
import re
import numpy as np 

def dig(x,y,i,arr):
    amt = directions[i][1]
    direct = directions[i][0]
    dx, dy = dirs[direct]
    curr = direct
    next = directions[(i+1)%len(directions)][0]

    x, y = x+dx*(amt), y+dy*(amt)
    curr = "".join(sorted([curr,next]))
    #Change coords based on what type of corner it is
    if curr == "01":
        arr.append(x+1)
        arr.append(y)
    elif curr == "12":
        arr.append(x+1)
        arr.append(y+1)
    elif curr == "23":
        arr.append(x)
        arr.append(y+1)
    else:
        arr.append(x)
        arr.append(y)
    return x, y

with open("Day 18/input.txt") as f:
    dirs = {"0": (1,0), "1": (0,1), "2": (-1,0), "3": (0,-1)}
    trench = {}

    arr = []
    directions = []

    for line in f:
        color = re.search("#[0-9a-f]+", line).group(0)
        amount = int(color[1:-1],16)
        direction = color[-1]
        directions.append((direction,amount))
    x, y = 0,0  
    for i in range(len(directions)):
        x,y = dig(x,y,i,arr)
    
    #Use gauss's area formula
    arr = np.array(arr,dtype='int64')
    arr = np.reshape(arr,(-1,2))
    x = (arr[:,0])
    y = (arr[:,1])
    
    s1 = np.sum(x*np.roll(y,-1))
    s2 = np.sum(y*np.roll(x,-1))
    total = int(0.5*np.abs(s1-s2))

    print("Part 2:", total)