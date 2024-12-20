import typing

def read_file(file_path: str) -> list:
    with open(file_path, 'r') as input:
        content = input.readlines()
        return content

def get_sum(file):
    sum = 0
    for line in file:
        id, game = line.split(": ")
        game_id = id.split()[-1]
        print("game_id: ", game_id)
        rounds = game.split("; ")
        print("rounds: " , rounds)
        minimum_cubes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for round in rounds:
            combos = [x.split() for x in round.split(", ")]
            print("combination: ", combos)
            counts = {}
            for count, colour in combos:
                counts[colour] = int(count)
            print(counts)
            minimum_cubes["red"] = max(minimum_cubes["red"], counts.get("red", 0))
            print(minimum_cubes["red"])
            minimum_cubes["green"] = max(minimum_cubes["green"], counts.get("green", 0))
            print(minimum_cubes["green"])
            minimum_cubes["blue"] = max(minimum_cubes["blue"], counts.get("blue", 0))
            print(minimum_cubes["blue"])
            minimum_power = minimum_cubes["red"] * minimum_cubes["green"] * minimum_cubes["blue"]
            print("minimum power: ", minimum_power)
        sum += minimum_power    
    return sum

if __name__ == "__main__":
    a_list = read_file('./day_02/input.txt')
    print(get_sum(a_list))
