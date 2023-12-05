import re

def read_file(input: str) -> list:
    with open(input, "r") as file:
        input_list = [[set[1].strip().split("|")] for set in [line.strip().split(":") for line in file]]
        return input_list

day4_data = read_file("2023/Day_4/day4_input.txt")

def compare_cards(input_list: list) -> list:
    numbers = []
    points = []
    for list in input_list:
        for item in list:
            winning_nums = re.findall(r'\b\d+\b', item[0])
            my_nums = re.findall(r'\b\d+\b', item[1])
            numbers.append((winning_nums, my_nums))
    points.extend(len([win_num for win_num in set[0] for my_num in set[1] if win_num == my_num]) for index, set in enumerate(numbers))
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

result_part1 = sum(calculate_points(day4_data))
print(f'Part 1: {result_part1}')


def part2(input_list: list) -> int:
    points = compare_cards(input_list)
    cards = [1] * len(points)
    for index, point in enumerate(points):
        nums = point
        while nums:
            cards[index + nums] += cards[index]
            nums -= 1
    return cards

result_part2 = sum(part2(day4_data))
print(f'Part 2: {result_part2}')

                
    
