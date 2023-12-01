def read_file(input: str) -> list:
    with open(input, "r") as file:
        #Read each line of the file
        input_list = file.read().strip().split("\n")
        return input_list

day1_data = read_file("2023/Day 1/day1_input.txt")

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