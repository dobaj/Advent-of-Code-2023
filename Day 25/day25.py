import random, copy
def karger(graph: dict):
    while len(graph) > 2:
        v = random.choice(list(graph.keys()))
        w = random.choice(list(graph[v][0]))
        contract(graph, v, w)
    return len(graph[list(graph.keys())[0]][0]), graph

def contract(graph, v, w):
    #Keep track of how many nodes have been contracted into this one
    graph[v][1] += graph[w][1]
    for n in graph[w][0]:
        if n != v:
            #Avoid self loops
            graph[v][0].append(n)
            graph[n][0].append(v)
        graph[n][0].remove(w)
    graph.pop(w)

with open("Day 25/input.txt") as f:
    graph = {}
    for line in f:
        line = line.strip().split(":")
        node = line[0]
        neigh = line[1].split()
        if node in graph:
            for n in neigh:
                graph[node][0].append(n)
        else:
            graph[node] = [neigh,1]
        for n in neigh:
            if n in graph:
                graph[n][0].append(node)
            else:
                graph[n] = [[node],1]

    old_graph = copy.deepcopy(graph)
    cuts = 0
    while cuts != 3: #We know min cut is 3
        graph = copy.deepcopy(old_graph)
        cuts, graph = karger(graph)
    
    prod = 1
    for g in graph:
        prod *= graph[g][1]
    print("Part 1:", prod)
    print("Part 2:", "Button Pressed!")