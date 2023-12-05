# Part 1
sum = 0
maximums = {"red": 12, "green": 13, "blue": 14}
with open("Day 02/input.txt") as f:
    for line in f:
        id = int(line.split()[1][:-1])
        games = line[line.index(":")+2:] # add 2 to account for space
        for game in games.split(";"):
            for cube in game.split(","):
                cube = cube.split()
                if maximums[cube[1]] < int(cube[0]):
                    id = 0
        sum+=id
print("Part 1:",sum)

# Part 2
sum = 0
with open("Day 2/input.txt") as f:
    for line in f:
        maximums = {"red": 0, "green": 0, "blue": 0}
        games = line[line.index(":")+2:] # add 2 to account for space
        for game in games.split(";"):
            for cube in game.split(","):
                cube = cube.split()
                maximums[cube[1]] = max(maximums[cube[1]],int(cube[0]))
        power = 1
        for val in maximums.values():
            power*=val
        sum+=power
print("Part 2:",sum)