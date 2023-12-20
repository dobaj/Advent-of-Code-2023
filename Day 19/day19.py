#Part 1
def eval_part(label):
    if label == "R":
        return False
    if label == "A":
        return True
    rules = exprs[label]
    i = 0
    while i < len(rules):
        if ">" in rules[i]:
            if values[rules[i][0]] > int(rules[i][2:]):
                return eval_part(rules[i+1])
            else:
                #skip over the label
                i+=2
        elif "<" in rules[i]:
            if values[rules[i][0]] < int(rules[i][2:]):
                return eval_part(rules[i+1])
            else:
                i+=2
        else:
            return eval_part(rules[i])


with open("Day 19/input.txt") as f:
    total = 0
    exprs = {}
    values = {}

    line = f.readline()
    while line != "\n":
        #ignore \n and ending curly bracket
        line = (line[:-2])
        line = (line.split("{"))
        label = line[0]
        #split all rules
        line = (line[1].split(","))
        rules = []
        for l in line:
            rules.extend(l.split(":"))
        exprs[label] = rules
        line = f.readline()
    line = f.readline()
    while line:
        line = line.strip()[1:-1]
        for l in line.split(","):
            l=l.split("=")
            values[l[0]] = int(l[1])
        if (eval_part("in")):
            total += sum(list(values.values()))
        line = f.readline()
    print("Part 1:", total)

#Part 2
def eval_part(values,label):
    if label == "R":
        return
    if label == "A":
        global total
        tot = 1
        for v in values:
            tot *= (values[v][1]-values[v][0]+1)
        total += tot
        return
    rules = exprs[label]
    i = 0
    while i < len(rules):
        if ">" in rules[i]:
            letter = rules[i][0]
            comp = int(rules[i][2:])
            tup = values[letter]
            if tup[1] > comp:
                val2 = values.copy()
                val2[letter] = (max(comp+1,tup[0]), tup[1])
                eval_part(val2,rules[i+1])
                if tup[0] > comp:
                    return
                values[letter] = (tup[0], comp)
            i+=2
        elif "<" in rules[i]:
            letter = rules[i][0]
            comp = int(rules[i][2:])
            tup = values[letter]
            if tup[0] < comp:
                val2 = values.copy()
                val2[letter] = (tup[0], min(comp-1,tup[1]))
                eval_part(val2,rules[i+1])
                if tup[1] < comp:
                    return
                values[letter] = (comp, tup[1])
            i+=2
        else:
            eval_part(values,rules[i])
            i+=1


with open("Day 19/input.txt") as f:
    max_range = (1,4000)
    total = 0
    exprs = {}
    values = {}

    line = f.readline()
    while line != "\n":
        #ignore \n and ending curly bracket
        line = (line[:-2])
        line = (line.split("{"))
        label = line[0]
        #split all rules
        line = (line[1].split(","))
        rules = []
        for l in line:
            rules.extend(l.split(":"))
        exprs[label] = rules
        line = f.readline()
    
    values = {"x": max_range, "m": max_range, "a": max_range, "s": max_range}
    eval_part(values,"in")

    print("Part 2:", total)