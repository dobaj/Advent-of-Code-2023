#Part 1
with open("Day 14/input.txt") as f:
    rocks = []
    for line in f:
        rocks.append(line)

    max_load = [len(rocks)]*len(rocks[0])

    sum = 0

    for i in range(len(rocks)):
        for j in range(len(rocks[i])):
            if rocks[i][j] == "#":
                max_load[j] = len(rocks)-i-1
            if rocks[i][j] == "O":
                sum+=max_load[j]
                max_load[j]-=1
    
    print("Part 1:",sum)

#Part 2
roll_memo = {}
cycle_memo = {}

def roll(row):
    if row in roll_memo:
        return roll_memo[row]
    rocks = 0 #How many rocks to stack
    last = 0 #Last hash mark
    new = ""
    for i in range(len(row)):
        if row[i] == "O":
            rocks+=1
        elif row[i] == "#":
            new+="O"*rocks+"."*(i-last-rocks)+"#"
            last = i+1
            rocks = 0
    new+="O"*rocks+"."*(i+1-last-rocks)
    #Store result to increase performance
    roll_memo[row] = new
    return new

def cycle(rocks):
    s_rocks = str(rocks)
    for x in range(4):
        #Rotate array 90 deg and calculate roll
        new = []
        for i in range(len(rocks[0])):
            row = ""
            for j in range(len(rocks)):
                row+=rocks[j][i]
            new.append(roll(row)[::-1])
        rocks = new
    #Store to help identify loop
    cycle_memo[s_rocks] = rocks
    return rocks


with open("Day 14/input.txt") as f:
    rocks = []
    cycles = 1000000000
    for line in f:
        rocks.append(line.strip())

    sum = 0
    loop_len = 1

    i = 0
    while i < cycles:
        rocks = cycle(rocks)
        i+=1
        if str(rocks) in cycle_memo:
            #We have found a loop
            keys = list(cycle_memo.keys())
            for j in range(len(keys)):
                #Find index of the start of the loop
                if keys[j] == str(rocks):
                    loop_len = i-j
                    break
            if loop_len != 1:
                break
            
    for x in range((cycles-i)%loop_len):
        # Since rocks loop, only need to 
        # recalculate the remainder of the loop_len
        rocks = cycle(rocks)

    #Add load
    for r in range(len(rocks)):
        for j in rocks[r]:
            if j == "O":
                sum+=len(rocks)-r
        # print(rocks[r])

    print("Part 2:",sum)