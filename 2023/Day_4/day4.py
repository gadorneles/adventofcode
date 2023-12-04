import re

def read_file(input: str) -> list:
    with open(input, "r") as file:
        input_list = [line.strip().split(":") for line in file]
        separated_list = [[set[1].strip().split("|")] for set in input_list]
        return separated_list

day4_data = read_file("2023/Day_4/day4_input.txt")

def compare_cards(input_list: list) -> list:
    numbers = []
    points = []
    for list in input_list:
        for item in list:
            winning_nums = re.findall(r'\b\d+\b', item[0])
            my_nums = re.findall(r'\b\d+\b', item[1])
            numbers.append((winning_nums, my_nums))
    for index, set in enumerate(numbers):
        card = []
        for win_num in set[0]:
            for my_num in set[1]:
                if win_num == my_num:
                    card.append(win_num)
        points.append(len(card))
    return points

def calculate_points(input_list: list) -> int:
    points = compare_cards(input_list)
    results = []
    for point in points:
        if point > 0:
            result = 2 ** (point-1)
            results.append(result)
        else:
            results.append(0)

    return results

result = calculate_points(day4_data)
print(sum(result))
        
    
