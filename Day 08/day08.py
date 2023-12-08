import re
#Part 1
with open("Day 08/input.txt") as f:
    #Read in instructions/nodes
    instructions = f.readline()[:-1]
    f.readline()
    nodes = {}
    for line in f:
        line = re.findall("[A-Z]{3}",line)
        nodes[line[0]] = (line[1],line[2])
    
    current_node = "AAA"
    i = 0
    while current_node != "ZZZ":
        direction = instructions[i%len(instructions)]
        if direction == "L":
            current_node = nodes[current_node][0]
        else:
            current_node = nodes[current_node][1]
        i+=1
    print("Part 1:", i)

#Part 2
def gcd(a, b):
    # Euclidean algorithm
    if a % b == 0:
        return b
    return gcd(b, a%b)

with open("Day 08/input.txt") as f:
    #Read in instructions/nodes
    instructions = f.readline()[:-1]
    f.readline()
    nodes = {}
    start_nodes = []
    for line in f:
        for x in re.findall("[0-9A-Z]{2}A", line):
            start_nodes.append([x,""])
        line = re.findall("[0-9A-Z]{3}",line)
        nodes[line[0]] = (line[1],line[2])

    i = 0
    loops = []
    while start_nodes:
        #Current direction
        direction = instructions[i% len(instructions)]
        i+=1
        index = 1 # right
        if direction == "L":
            index = 0 # left
        
        # Run through each node
        for j in range(len(start_nodes)):
            start_nodes[j][1]+=start_nodes[j][0] # add to looper
            start_nodes[j][0] = nodes[start_nodes[j][0]][index]
        
        remove_nodes = []
        k = 0
        while k < len(start_nodes):
            string = start_nodes[k][1]
            #The string of visited nodes is a loop if this same z 
            # occurred a multiple of the instruction length ago
            if len(string) % len(instructions) == 0:
                if string[0:3] == start_nodes[k][0]:
                    start_nodes.pop(k)
                    loops.append(len(string)//3) #3 to account for length of node name
            if string[2] != "Z": # Reset if there is no Z at beginning of loop
                start_nodes[k][1] = ""
            k+=1

    #Find the LCM of all of the loop lengths
    for i in range(len(loops)-1):
        loops[i+1] = loops[i]//gcd(loops[i],loops[i+1])*loops[i+1]
    print("Part 2:", loops[-1])