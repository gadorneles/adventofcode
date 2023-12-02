def read_file(input: str) -> list:
    with open(input, "r") as file:
        #Read each line of the file
        input_list = file.read().strip().split("\n")
        return input_list

day1_data = read_file("2023/Day_1/day1_input.txt")

def calibration_values(input_list: list) -> int:
    total = 0
    for line in input_list:
        digits = []
        for char in line:
            if char.isdigit():
                digits.append(char)
        value = int(digits[0] + digits[-1])
        total += value
    return total

result = calibration_values(day1_data)
print(result)

def replace_spelled_numbers(input_list: list) -> list:
    new_list = []
    for line in input_list:
        line = (
        line.replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine")
        )
        new_list.append(line)
    return new_list
    
list_part2 = replace_spelled_numbers(day1_data)
result_2 = calibration_values(list_part2)
print(result_2)

