# Part 1
def find_diffs(diffs):
    all_0 = True
    for c in diffs:
        if c != 0:
            all_0 = False
            break
    if all_0 or len(diffs) < 2:
        return diffs[-1]
    new_diffs = []
    for i in range(len(diffs)-1):
        new_diffs.append(int(diffs[i+1])-int(diffs[i]))
    return find_diffs(new_diffs) + diffs[-1]
    
with open("Day 09/input.txt") as f:
    sum = 0
    for line in f:
        diffs = list(map(int,line.split()))
        # Find/ add up diffs recursively
        sum+=find_diffs(diffs)
    print("Part 1:", sum)

# Part 2
def find_diffs(diffs):
    # Find diffs in both directions
    all_0 = True
    for c in diffs:
        if c != 0:
            all_0 = False
            break
    if all_0 or len(diffs) < 2:
        return (diffs[0], diffs[-1])
    new_diffs = []
    for i in range(len(diffs)-1):
        new_diffs.append(int(diffs[i+1])-int(diffs[i]))
    last_diff = find_diffs(new_diffs)
    return (diffs[0] - last_diff[0], last_diff[1] + diffs[-1])
    
with open("Day 09/input.txt") as f:
    sum = 0
    for line in f:
        diffs = list(map(int,line.split()))
        # Find difference going backwards
        sum += find_diffs(diffs)[0]
    print("Part 2:", sum)
