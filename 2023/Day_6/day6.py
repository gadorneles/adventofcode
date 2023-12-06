def read_file(input: str) -> list:
    with open(input, "r") as file:
        input_list = [int(item) for line in file.read().split("\n") for item in line.split(' ')[1:] if item != '']
        return input_list

day6_data = read_file("2023/Day_6/day6_input.txt")

def part1(input_list: list) -> int:
    times = [i for i in input_list[:4]]
    records = [i for i in input_list[4:]]
    possible_times = []
    product = 1

    for index, time in enumerate(times):
        record = records[index]
        valid_times = []
        for i in range(0, time):
            new_time = time - i
            distance = i * new_time
            if distance > record:
                valid_times.append(new_time)
        possible_times.append(len(valid_times))     
        
    
    for element in possible_times:
        product *= element
    return product
        

result_part1 = part1(day6_data)
print(f'Part 1: {result_part1}')

def part2(input_list: list) -> int:
    time = int("".join(map(str, input_list[:4])))
    record = int("".join(map(str, input_list[4:])))
    valid_times = []

    for i in range(0, time):
        new_time = time - i
        distance = i * new_time
        if distance > record:
            valid_times.append(new_time)
    possible_times = len(valid_times)     
        
    return possible_times

result_part2 = part2(day6_data)
print(f'Part 2: {result_part2}')