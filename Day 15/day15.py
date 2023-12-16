#Part 1
with open("Day 15/input.txt") as f:
    line = f.readline()
    sum = 0
    for label in line.split(","):
        hash = 0
        for c in label:
            hash+=ord(c)
            hash*=17
            hash%=256
        sum+=hash
    print("Part 1:", sum)
    
#Part 2
with open("Day 15/input.txt") as f:
    map = []
    for x in range(256):
        # Initialize map with empty arrays
        map.append([])
    line = f.readline()
    operation = ""
    focal_len = 0
    for label in line.split(","):
        if "=" in label:
            operation = "="
            focal_len = int(label[-1]) #Always one digit num
            label = label[:-2]
        else:
            operation = "-"
            label = label[:-1]
        
        #Hash the label
        hash = 0
        for c in label:
            hash+=ord(c)
            hash*=17
            hash%=256
        
        if operation == "=":
            set_label = False
            for i in range(len(map[hash])):
                if map[hash][i][0] == label:
                    # Store as tuple so label can be compared
                    map[hash][i] = (label,focal_len) 
                    set_label = True
                    break
            if not set_label:
                map[hash].append((label, focal_len))
        else:
            i = 0
            while i < len(map[hash]):
                if map[hash][i][0] == label:
                    for j in range(i,len(map[hash])-1):
                        map[hash][j] = map[hash][j+1]
                    map[hash] = map[hash][:-1]
                    break
                i+=1

    sum = 0
    #Add up focusing power
    for i in range(len(map)):
        for j in range(len(map[i])):
            power = map[i][j][1]*(i+1)*(j+1)
            # print(map[i][j][0], power)
            sum+=power
    print("Part 2:",sum)
    