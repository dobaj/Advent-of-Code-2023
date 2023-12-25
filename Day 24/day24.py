#Part 1
def same_sign(x1,x2):
    return (x1 <= 0 and x2 <= 0) or (x1 > 0 and x2 > 0) 

def in_range(n):
    return n >= 200000000000000 and n <= 400000000000000 

with open("Day 24/input.txt") as f:
    sum = 0
    equations = [] # in form y = mx + b
    for line in f:
        line = (line.strip().split("@"))
        x,y,z = map(int,line[0].split(","))
        dx,dy,dz = map(int,line[1].split(","))
        m = dy/dx
        equations.append((1,m,-m*x + y, x, y, z, dx, dy, dz))

    for i in range(len(equations)):
        e = equations[i]
        for j in range(i+1,len(equations)):
            f = equations[j]
            x=(f[1]-e[1])
            b=(e[2]-f[2])
            if x == 0:
                continue
            x = (b/x)
            x,y = (x,e[1]*x+e[2])
            if same_sign(x-e[3],e[6]) and same_sign(x-f[3],f[6]):
                if in_range(x) and in_range(y):
                    sum+=1
    
    print("Part 1:", sum)


#Part 2
import z3

with open("Day 24/input.txt") as f:
    n = 300
    equations = [] # in form y = mx + b
    for line in f:
        line = (line.strip().split("@"))
        x,y,z = map(int,line[0].split(","))
        dx,dy,dz = map(int,line[1].split(","))
        equations.append(((x, y, z), (dx, dy, dz)))
    
    t = [z3.Real(f"t{i}") for i in range(n)]
    x,y,z = z3.Real("x"), z3.Real("y"), z3.Real("z")
    dx,dy,dz = z3.Real("dx"), z3.Real("dy"), z3.Real("dz")
    solver = z3.Solver()

    for i, e in enumerate(equations[:n]):
        p,v = (e[0],e[1])
        solver.add(p[0]+v[0]*t[i] == x + dx*t[i])
        solver.add(p[1]+v[1]*t[i] == y + dy*t[i])
        solver.add(p[2]+v[2]*t[i] == z + dz*t[i])
    res = solver.check()
    M = solver.model()

    print("Part 2:",M.eval(x+y+z))