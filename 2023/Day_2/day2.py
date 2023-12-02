def read_file(input: str) -> list:
    with open(input, "r") as file:
        # Read each line of the file
        input_list = file.read().strip().split("\n")
        return input_list

day1_data = read_file("2023/Day_2/day2_input.txt")

def split_games(input_list: list) -> dict:
    game_data = dict()
    
    for line in input_list:
        game_id, game_cubes = line.split(":")
        cube_data = game_cubes.split(";")
        
        game_data[game_id] = []  
        
        for cubes in cube_data:
            cubes = cubes.strip().split(",")
            for item in cubes:
                quantity, color = item.strip().split(" ")
                cube_data_dict = {'Quantity': int(quantity), 'Color': color}
                game_data[game_id].append(cube_data_dict)

    return game_data


game_dict = split_games(day1_data)

def possible_games(input_dict: dict) -> list:
    maximum_cubes = [
        {'Quantity': 12, 'Color': 'red'}, 
        {'Quantity': 13, 'Color': 'green'}, 
        {'Quantity': 14, 'Color': 'blue'}
    ]

    possible_games = []

    for game_id, game_cubes in input_dict.items():
        valid_game = True
        for cube in game_cubes:
            for cubes in maximum_cubes:
                if cube["Color"] == cubes["Color"] and cube["Quantity"] > cubes["Quantity"]:
                        valid_game = False
                        break
                
        if valid_game:
            possible_games.append(game_id)

    return possible_games
    
games = possible_games(game_dict)

def games_sum(input_list: list) -> int:
    total = 0
    for item in input_list:
        _ , value = item.split(" ")
        value = int(value)
        total += value
    return total

result_part1 = games_sum(games)
print(f'Part 1: {result_part1}')

def fewest_cubes(input_dict: dict) -> int:
    cube_set_power = []
    for game_id, game_cubes in input_dict.items():
        minimum_cubes = {
            "green": 0,
            "blue": 0,
            "red": 0
        }
        
        for cube in game_cubes:
            if cube["Color"] == "green":
                if cube["Quantity"] > minimum_cubes["green"]:
                    minimum_cubes["green"] = cube["Quantity"]
            elif cube["Color"] == "blue":
                if cube["Quantity"] > minimum_cubes["blue"]:
                    minimum_cubes["blue"] = cube["Quantity"]
            elif cube["Color"] == "red":
                if cube["Quantity"] > minimum_cubes["red"]:
                    minimum_cubes["red"] = cube["Quantity"]
        
        cube_set_power.append(minimum_cubes["green"] * minimum_cubes["blue"] * minimum_cubes["red"])
    
    power_sum = sum(cube_set_power)
    return power_sum

result_part2= fewest_cubes(game_dict)
print(f'Part 2: {result_part2}')
        
        


        

    
                