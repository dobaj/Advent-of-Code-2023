import re
# Part 1
with open("Day 4/input.txt") as f:
    card_sum = 0
    for line in f:
        card = 0
        line = line.split(":")[1].split("|")
        win_nums = set()
        # Injest winning nums
        for num in re.findall("[0-9]+",line[0]):
            win_nums.add(num) # Doesnt need to be int
        # Find matching nums
        for num in re.findall("[0-9]+",line[1]):
            if num in win_nums:
                if card == 0:
                    card = 1
                else:
                    card *= 2
        card_sum+=card
print("Part 1:", card_sum)

# Part 2
with open("Day 4/input.txt") as f:
    lines = f.readlines()
    cards_length = len(lines)
    cards = [1]*cards_length # Fill with 1 by default
    for i, line in enumerate(lines):
        multiplier = cards[i]
        card_copies = 0
        line = line.split(":")[1].split("|")
        win_nums = set()
        # Injest winning nums
        for num in re.findall("[0-9]+",line[0]):
            win_nums.add(num) # Doesnt need to be int
        # Find matching nums
        for num in re.findall("[0-9]+",line[1]):
            if num in win_nums:
                card_copies+=1
        # Add copies
        for j in range(i+1,min(i+card_copies+1, cards_length)):
            cards[j]+=multiplier
print("Part 2:", sum(cards))
