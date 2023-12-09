def read_file(input: str) -> list:
    with open(input, "r") as file:
        # Read each line of the file
        input_list = [(x.split()) for x in file.read().split("\n")]
        return input_list
    
day7_data = read_file("2023/Day_7/day7_input.txt")

def part1(input_file: list) -> int:
    sorted_hands = []
    winnings = 0

    for hand, bid in input_file:
        card_indices = list(map("*23456789TJQKA".index, hand))
        counts = [hand.count(card) for card in hand]

        #Possible hands:
        if 5 in counts:
            type = 6
        elif 4 in counts:
            type = 5
        elif 3 in counts:
            if 2 in counts:
                type = 4
            else:
                type = 3
        elif counts.count(2) == 4:
            type = 2
        elif 2 in counts:
            type = 1
        else:
            type = 0

        sorted_hand = [(type), card_indices,(int(bid))]
        sorted_hands.append(sorted_hand)
    
    sorted_hands.sort(key=lambda x: (x[0], x[1]))

    for index, hand in enumerate(sorted_hands):
        winnings += hand[2] * (index + 1)
    return winnings
        
result_part1 = part1(day7_data)
print(f'Part 1: {result_part1}')