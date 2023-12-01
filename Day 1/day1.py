import re
# Part 1
with open("Day 1/input.txt") as f:
    sum = 0
    for line in f:
        numbers = re.findall("[1-9]",line)
        first, last = numbers[0], numbers[-1]
        sum += int(first + last)
print("Part 1:", sum)  

# Part 2
with open("Day 1/input.txt") as f:
    sum = 0
    for line in f:
        number_map = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
        numbers = re.findall("(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))",line)
        first, last = numbers[0], numbers[-1]
        output = ""
        for num in (first,last):
            if num in number_map:
                output+=str(number_map[num])
            else:
                output+=num
        sum += int(output)

print("Part 2:", sum)