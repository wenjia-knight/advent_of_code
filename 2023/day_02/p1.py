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
        print(game_id)
        rounds = game.split("; ")
        print(rounds)
        for round in rounds:
            combos = [x.split() for x in round.split(", ")]
            print(combos)
            counts = {}
            for count, colour in combos:
                counts[colour] = int(count)
            print(counts)
            if not (counts.get("red", 0) <= 12 and counts.get("green", 0) <= 13 and counts.get("blue", 0) <= 14):
                break
        else:
            sum += int(game_id)
    return sum

if __name__ == "__main__":
    a_list = read_file('./day_02/input.txt')
    print(get_sum(a_list))

