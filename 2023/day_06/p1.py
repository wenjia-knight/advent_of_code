import math

def read_file(file_path: str) -> list:
    with open(file_path, 'r') as input:
        content = input.read().splitlines()
        return content
    
def ways_to_win(a_time: int, a_dist: int) -> int:
    ways_to_win = 0
    for i in range(a_time+1):
        hold_button = i
        print("hold button for ", hold_button, " ms")
        travel_time =  a_time - hold_button
        print("travel for ", travel_time, " ms")
        travel_dist = i * travel_time
        print("travel distance: ", travel_dist)
        if travel_dist > a_dist:
            ways_to_win += 1
    return ways_to_win

if __name__ == "__main__":
    a_list = read_file('./day_06/example.txt')
    print(a_list)
    time_list = [int(x) for x in a_list[0].split(":")[1].strip().split()]
    print(time_list)
    distance_list = [int(x) for x in a_list[1].split(":")[1].strip().split()]
    print(distance_list)
    dict = dict(zip(time_list, distance_list))
    print(dict)
    ways_to_win = [ways_to_win(i, dict[i]) for i in time_list]
    print(ways_to_win)
    print(math.prod(ways_to_win))
