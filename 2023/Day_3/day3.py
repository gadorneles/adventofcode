import re

def read_file(input: str) -> list:
    with open(input, "r") as file:
        # Read each line of the file
        input_list = file.read().strip().split("\n")
        return input_list

day1_data = read_file("2023/Day_3/day3_input.txt")

def find_numbers(input_list: list) -> list:
    numbers_list = []

    for index, string in enumerate(input_list):
        numbers = re.finditer(r'\b\d+\b', string)
        for match in numbers:
            number = int(match.group())
            position_start = match.start()
            numbers_list.append((number, position_start, index))
    return numbers_list


def find_neighbors(input_list: list) -> list:
    numbers = find_numbers(input_list)
    valid_numbers = []

    for index, string in enumerate(input_list):
        previous_string = input_list[index - 1] if index - 1 >= 0 else string
        next_string = input_list[index + 1] if index + 1 < len(input_list) else string

        for number in numbers:
            ValidNumber = False
            if number[2] == index:
                length = len(str(number[0]))
                range_x = range(number[1] - 1, number[1] + length + 1)
                for value in range_x:
                    if value >= 140:
                        break
                    elif any(
                        s[value] != "." and not s[value].isdigit()
                        for s in [previous_string, next_string, string]
                    ):
                        ValidNumber = True
                        break
            if ValidNumber:
                valid_numbers.append(number[0])
    return valid_numbers

result_part1 = sum(find_neighbors(day1_data))
print(f'Part 1: {result_part1}')

                
