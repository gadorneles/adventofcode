def read_file(input: str) -> list:
    with open(input, "r") as file:
        # Read each line of the file
        input_list = file.read().split("\n\n")
        return input_list
    
day5_data = read_file("2023/Day_5/day5_input.txt")

def part1(input_file: list) -> int:
    seeds = [int(y) for y in input_file[0].split(':')[1].strip().split(" ")]
    

    for block in input_file[1:]:
        ranges = [[int(y) for y in x.split(' ')] for x in block.split('\n')[1:]]
        new_list = []
        for seed in seeds:
            for destination, source, length in ranges:
                if source <= seed < source + length:
                    new_list.append(seed - source + destination)
                    break
            else:
                new_list.append(seed)
        seeds = new_list
    return seeds
                    
result_part1 = min(part1(day5_data))
print(f'Part 1: {result_part1}')


#Part 2 seems to be working but it consumes too much memory and takes too long to run.
# def part2(input_file: list) -> int:
#     seeds = [int(y) for y in input_file[0].split(':')[1].strip().split(" ")]
#     new_seeds = []
    
#     for index, seed in enumerate(seeds):
#         if index % 2 == 0:
#             for i in range(seeds[index+1]):
#                 new_seeds.append(seed)
#                 seed = seed + 1

#     seeds = new_seeds

#     for block in input_file[1:]:
#         ranges = [[int(y) for y in x.split(' ')] for x in block.split('\n')[1:]]
#         new_list = []
#         for seed in seeds:
#             for destination, source, length in ranges:
#                 if source <= seed < source + length:
#                     new_list.append(seed - source + destination)
#                     break
#             else:
#                 new_list.append(seed)
#         seeds = new_list
#     return seeds

# result_part2 = min(part2(day5_data))
# print(f'Part 2: {result_part2}') 