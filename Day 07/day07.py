
#Part 1
def quick(arr, lo, hi):
    #Quicksort
    if lo >= hi or lo < 0:
        return
    pivot = arr[hi]
    i = lo-1

    for j in range(lo, hi):
        if compare_cards(arr[j],pivot) == -1:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    
    i+=1
    arr[i], arr[hi] = arr[hi], arr[i]
    quick(arr, lo, i-1)
    quick(arr, i+1, hi)

def compare_cards(card1, card2):
    #Compares cards first by hand type and then by card ranking
    if card1[1] > card2[1]:
        return 1
    elif card1[1] == card2[1]:
        i = 0
        while i < len(card1[0]) and card1[0][i] == card2[0][i]:
            i+=1
        if card_ordering.find(card1[0][i]) <= card_ordering.find(card2[0][i]):
            return 1
    return -1


with open("Day 07/input.txt") as f:
    card_ordering = "AKQJT98765432"
    hands = []
    for line in f:
        line = line.split()
        #Count card occurences
        cards = {}
        for c in line[0]:
            if c not in cards:
                cards[c] = 1
            else:
                cards[c] += 1
        #Sort by card count
        occurence_list = list(cards.values())
        occurence_list.sort(reverse=True)
        #Construct hand with cards, top two occurences, and bid
        hand = (line[0], occurence_list[:2], int(line[1]))
        hands.append(hand)

    quick(hands,0,len(hands)-1)
    sum = 0
    for rank, hand in enumerate(hands):
        sum += (rank+1)*hand[2]
    print("Part2:",sum)

#Part 2
def quick(arr, lo, hi):
    if lo >= hi or lo < 0:
        return
    pivot = arr[hi]
    i = lo-1

    for j in range(lo, hi):
        if compare_cards(arr[j],pivot) == -1:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    
    i+=1
    arr[i], arr[hi] = arr[hi], arr[i]
    quick(arr, lo, i-1)
    quick(arr, i+1, hi)

def compare_cards(card1, card2):
    if card1[1] > card2[1]:
        return 1
    elif card1[1] == card2[1]:
        i = 0
        while i < len(card1[0]) and card1[0][i] == card2[0][i]:
            i+=1
        if card_ordering.find(card1[0][i]) <= card_ordering.find(card2[0][i]):
            return 1
    return -1


with open("Day 07/input.txt") as f:
    card_ordering = "AKQT98765432J"
    hands = []
    for line in f:
        line = line.split()
        max_occurence, max_card = 0, ""
        #Count occurences per letter
        cards = {}
        for c in line[0]:
            if c not in cards:
                cards[c] = 1
            else:
                cards[c] += 1
            #Highest non J
            if cards[c] > max_occurence and c != "J":
                max_occurence = cards[c]
                max_card = c
        #Add J to the highest non J card count and remove from cards
        if "J" in cards and max_card:
            cards[max_card] += cards.pop("J")
        #Sort by card count
        occurence_list = list(cards.values())
        occurence_list.sort(reverse=True)
        #Construct hand with cards, top two occurences, and bid
        hand = (line[0], occurence_list[:2], int(line[1]))
        hands.append(hand)
    quick(hands,0,len(hands)-1)
    sum = 0
    for rank, hand in enumerate(hands):
        sum += (rank+1)*hand[2]
    print("Part2:",sum)