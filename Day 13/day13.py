#Part 1
def is_ref_vert(i, arr):
    #Choose indices based on which edge is closer
    if i > len(arr[0])//2:
        left_i = 2*i - len(arr[0])
        right_i = len(arr[0])-1
    else:
        left_i = 0
        right_i = 2*i-1

    for x in arr:
        if x[left_i:i] != x[right_i:i-1:-1]:
            return 0
    return i

def is_ref_horiz(i, arr):
    #Choose indices based on which edge is closer
    if i > len(arr)//2:
        left_i = 2*i - len(arr)
        right_i = len(arr)-1
    else:
        left_i = 0
        right_i = 2*i-1
    
    j = 0
    while left_i+j < i:
        if arr[left_i+j] != arr[right_i-j]:
            return 0
        j+=1
    return 100*i

with open("Day 13/input.txt") as f:
    sum = 0
    patterns = []
    pattern = []
    for line in f:
        if line == "\n":
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(line.strip())
    #add last pattern
    patterns.append(pattern)

    for arr in patterns:
        mini_sum = 0
        for j in range(1,len(arr[0])):
            mini_sum+=is_ref_vert(j, arr)
        for x in range(1,len(arr)):
            mini_sum+=is_ref_horiz(x,arr)
        if mini_sum == 0:
            #Every pattern needs a reflection
            print(arr)
        sum+=mini_sum
    print("Part 1:", sum)

#Part 2
def diff(string1: str, string2: str):
    #Find number of differences in strings
    error_count = 0
    i = 0
    while i < len(string1):
        if string1[i] != string2[i]:
            error_count+=1
        i+=1
    return error_count

def is_ref_vert(i, arr):
    #Choose indices based on which edge is closer
    if i > len(arr[0])//2:
        left_i = 2*i - len(arr[0])
        right_i = len(arr[0])-1
    else:
        left_i = 0
        right_i = 2*i-1

    diffs = 0
    for x in arr:
        if x[left_i:i] != x[right_i:i-1:-1]:
            diffs+=diff(x[left_i:i], x[right_i:i-1:-1])
    # change from needing no errors to only one allowed
    if diffs == 1:
        return i
    return 0

def is_ref_horiz(i, arr):
    #Choose indices based on which edge is closer
    if i > len(arr)//2:
        left_i = 2*i - len(arr)
        right_i = len(arr)-1
    else:
        left_i = 0
        right_i = 2*i-1

    diffs = 0
    j = 0
    while left_i+j < i:
        if arr[left_i+j] != arr[right_i-j]:
            diffs+=diff(arr[left_i+j],arr[right_i-j])
        j+=1
    # change from needing no errors to only one
    if diffs == 1:
        return 100*i
    return 0

with open("Day 13/input.txt") as f:
    sum = 0
    patterns = []
    pattern = []
    for line in f:
        if line == "\n":
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(line.strip())
    #add last pattern
    patterns.append(pattern)

    for arr in patterns:
        mini_sum = 0
        for j in range(1,len(arr[0])):
            mini_sum+=is_ref_vert(j, arr)
        for x in range(1,len(arr)):
            mini_sum+=is_ref_horiz(x,arr)
        if mini_sum == 0:
            #Every pattern needs a reflection
            print(arr)
        sum+=mini_sum
    print("Part 2:", sum)