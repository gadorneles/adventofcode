def read_file(input: str) -> list:
    with open(input, "r") as file:
        # Read each line of the file
        input_list = [list(map(int, line.split())) for line in file]
        return input_list
    
day9_data = read_file("2023/Day_9/day9_input.txt")

def diff(input_list: list) -> list:
    diff_list = []
    for index, value in enumerate(input_list):
        if index == len(input_list)-1:
            break
        else:
            diff_value = input_list[index+1] - value
            diff_list.append(diff_value)
    return diff_list



def part1(input_list: list) -> int:
    values_sum = 0
    
    for history in input_list:
            values = [history]
            while any(history) != 0:
                history = diff(history)
                values.append(history)

            for index, value in enumerate(reversed(values)):
                if index == 0:
                    value.append(0)
                else:
                    value.append(value[-1] + list(reversed(values))[index-1][-1])

            values_sum += values[0][-1]
    return values_sum


result_part1 = part1(day9_data)
print(f'Part 1: {result_part1}')

def part2(input_list: list) -> int:
    values_sum = 0
    
    for history in input_list:
            values = [history]

            while any(history) != 0:
                history = diff(history)
                values.append(history)

            for index, value in enumerate(reversed(values)):
                if index == 0:
                    value.append(0)
                else:
                    value.insert(0, (value[0] - list(reversed(values))[index-1][0]))

            values_sum += values[0][0]
    return values_sum

result_part2 = part2(day9_data)
print(f'Part 2: {result_part2}')
