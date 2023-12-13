#Part 1
import re

def match(line, groups):
    if not groups:
        if not "#" in line:
            return [line.replace("?",".")]
        return []
    if not line:
        return []
    pattern = f"(?=([#?]{{{groups[0]}}}[?.]+))"
    periods = 1
    if len(groups) == 1:
        pattern = f"(?=([#?]{{{groups[0]}}}))"
        periods = 0
    
    matches = list(re.finditer(pattern,line))
    valid = []
    for mtch in matches:
        start = mtch.start()
        if "#" in line[:start]:
            continue
        ret = match(line[start+groups[0]+periods:], groups[1:])
        for x in ret:
            #Recreate permutation
            valid.append(line[:start].replace("?",".")+"#"*groups[0]+"."*periods+x)
    return valid


with open("Day 12/input.txt") as f:
    sum = 0
    for line in f:
        groups = list(map(int,re.findall("[0-9]+", line)))
        line = line.split()[0]

        mtch = match(line,groups)
        sum += len(mtch)

        # print(groups)
        # print(line)
        # for x in mtch:
        #     print(x)
        # print()

    print("Part 1:", sum)


#Part 2
import re
match_memo = {}

def match(line:str, groups):
    #New match that uses memoizing to increase perf
    #Does not recreate all permutations
    if (line, str(groups)) in match_memo:
        return match_memo[(line, str(groups))]
    if not groups:
        if not "#" in line:
            return 1
        return 0
    if not line:
        return 0

    perms = 0
    matches = []

    first = line.find("#")
    if first == -1:
        # if there is no hash, set to maximum possible
        first = len(line)-groups[0]
    else:
        first = min(first,len(line)-groups[0])

    start = 0
    while start <= first:
        valid = True
        for i in range(groups[0]):
            if line[start+i] != "#" and line[start+i] != "?":
                #If . then this is not valid for this group size
                valid = False
                break
        #Must end with either end of str or ? or .
        if valid and (start+i == len(line)-1 or line[start+i+1] == "?" or line[start+1+i] == "."):
            matches.append(min(start+i+2,len(line)))
        start+=1
    
    for m in matches:
        mtc = match(line[m:], groups[1:])
        perms+=mtc
    
    #store for memoizing
    match_memo[(line, str(groups))] = perms
    return perms

with open("Day 12/input.txt") as f:
    folds = 5
    sum = 0
    for line in f:
        groups = list(map(int,re.findall("[0-9]+", line)))
        line = line.split()[0]

        line =((line+"?")*folds)[:-1]
        groups = groups*folds
        mtch = match(line,groups)
        sum+=mtch
        
    print("Part 2:", sum)