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
        start_nodes += re.findall("[0-9A-Z]{2}A", line)
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
        
        # Run through each node. Remove once loop found
        j = 0
        while j < len(start_nodes):
            start_nodes[j] = nodes[start_nodes[j]][index]
            #Because paths start at the start of loop and only visit one z each
            if start_nodes[j][2] == "Z":
                loops.append(i)
                start_nodes.pop(j)
                continue
            j+=1

    #Find the LCM of all of the loop lengths
    for i in range(len(loops)-1):
        loops[i+1] = loops[i]//gcd(loops[i],loops[i+1])*loops[i+1]
    print("Part 2:", loops[-1])