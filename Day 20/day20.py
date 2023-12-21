#Part 1
import heapq
def run_module():
    Q = []
    heapq.heapify(Q)
    heapq.heappush(Q,(0,"broadcaster",0,""))

    global low, high

    while Q:
        i, name, signal, input = heapq.heappop(Q)
        if signal == 1:
            high+=1
        else:
            low+=1
        if name not in modules:
            continue
        mod = modules[name]
        i+=1

        if mod[0] == "B":
            pass
        elif mod[0] == "%":
            if signal == 0:
                if flip_mem[name] == 0:
                    signal = 1
                    flip_mem[name] = 1
                else:
                    signal = 0
                    flip_mem[name] = 0
            else:
                continue
                
        else:
            #conjunction
            conj_mem[input] = signal
            all_hi = True
            for x in conj_list[name]:
                if conj_mem[x] == 0:
                    all_hi = False
                    break
            if all_hi:
                signal = 0
            else:
                signal = 1
        for x in mod[1:]:
            heapq.heappush(Q,(i,x,signal,name))




with open("Day 20/input.txt") as f:
    low, high = 0, 0
    modules = {}
    flip_mem = {}
    conj_mem = {}
    conj_list = {}
    
    for line in f:
        line = line.strip().split(" -> ")
        out = (line[1].split(", "))
        if line[0] == "broadcaster":
            modules["broadcaster"] = ["B"]
            modules["broadcaster"].extend(out)
        else:
            modules[line[0][1:]] = [line[0][0]]
            modules[line[0][1:]].extend(out)
        flip_mem[line[0][1:]] = 0
        conj_mem[line[0][1:]] = 0

    for m in modules:
        for n in modules[m][1:]:
            if n in modules:
                if modules[n][0] == "&":
                    if n not in conj_list:
                        conj_list[n] = []
                    conj_list[n].append(m)

    for i in range(1000):
        run_module()
    print("Part 1:",low*high)

#Part 2
import heapq
def gcd(a, b):
    # Euclidean algorithm
    if a % b == 0:
        return b
    return gcd(b, a%b)

def run_module():
    Q = []
    heapq.heapify(Q)
    heapq.heappush(Q,(0,"broadcaster",0,""))

    global low, high

    cycle = []
    while Q:
        i, name, signal, input = heapq.heappop(Q)
        if signal == 1:
            high+=1
        else:
            low+=1
        if name not in modules:
            continue
        mod = modules[name]
        i+=1

        if mod[0] == "B":
            pass
        elif mod[0] == "%":
            if signal == 0:
                if flip_mem[name] == 0:
                    signal = 1
                    flip_mem[name] = 1
                else:
                    signal = 0
                    flip_mem[name] = 0
            else:
                continue
        else:
            #&
            conj_mem[input] = signal
            all_hi = True
            for x in conj_list[name]:
                if conj_mem[x] == 0:
                    all_hi = False
                    break
            if all_hi:
                signal = 0
            else:
                signal = 1

        if signal == 1 and name in conj_list[prev_conj]:
            cycle.append(name)

        for x in mod[1:]:
            heapq.heappush(Q,(i,x,signal,name))
    return cycle

with open("Day 20/input.txt") as f:
    modules = {}
    flip_mem = {}
    conj_mem = {}
    conj_list = {}
    prev_conj = "vf"

    
    for line in f:
        line = line.strip().split(" -> ")
        out = (line[1].split(", "))
        if line[0] == "broadcaster":
            modules["broadcaster"] = ["B"]
            modules["broadcaster"].extend(out)
        else:
            modules[line[0][1:]] = [line[0][0]]
            modules[line[0][1:]].extend(out)
            flip_mem[line[0][1:]] = 0
    
    for m in modules:
        for n in modules[m][1:]:
            if n in modules:
                if modules[n][0] == "&":
                    conj_mem[m] = 0
                    if n not in conj_list:
                        conj_list[n] = []
                    conj_list[n].append(m)

    i = 1
    loops = []
    loop_names = []
    while len(loops) < 4:
        for x in run_module():
            if x not in loop_names:
                loops.append(i)
                loop_names.append(x)
        i+=1
    
    for i in range(len(loops)-1):
        loops[i+1] = loops[i]//gcd(loops[i],loops[i+1])*loops[i+1]
    
    print("Part 2:", loops[-1])