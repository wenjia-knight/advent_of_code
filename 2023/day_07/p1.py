from collections import Counter

def read_file(file_path: str) -> list:
    with open(file_path, 'r') as input:
        content = input.read().splitlines()
        return content
    
def is_five_of_a_kind(a_string: str) -> bool:
    if Counter(a_string).most_common(1)[0][1] == 5:
        return True
    else:
        return False
    
def is_four_of_a_kind(a_string: str) -> bool:
    if Counter(a_string).most_common(1)[0][1] == 4:
        return True
    else:
        return False
    
def is_full_house(a_string: str) -> bool:
    if Counter(a_string).most_common(2)[0][1] == 3 and Counter(a_string).most_common(2)[1][1] == 2:
        return True
    else:
        return False

def is_three_of_a_kind(a_string: str) -> bool:
    if Counter(a_string).most_common(3)[0][1] == 3 and Counter(a_string).most_common(3)[1][1] == 1:
        return True
    else:
        return False    

def is_two_pair(a_string: str) -> bool:
    if Counter(a_string).most_common(2)[0][1] == 2 and Counter(a_string).most_common(2)[1][1] == 2:
        return True
    else:
        return False

def is_one_pair(a_string: str) -> bool:
    if Counter(a_string).most_common(2)[0][1] == 2 and Counter(a_string).most_common(2)[1][1] != 2:
        return True
    else:
        return False

def is_high_card(a_string: str) -> bool:
    if len(list(a_string)) == len(set(list(a_string))):
        return True
    else:
        return False
    
def check_hand_type(a_string: str) -> int:
    if is_five_of_a_kind(a_string) == True:
        return 7
    elif is_four_of_a_kind(a_string) == True:
        return 6
    elif is_full_house(a_string) == True:
        return 5
    elif is_three_of_a_kind(a_string) == True:
        return 4
    elif is_two_pair(a_string) == True:
        return 3
    elif is_one_pair(a_string) == True:
        return 2
    else:
        return 1
    
def check_strength(hand):
    return (check_hand_type(hand), [letter_map.get(card, card) for card in hand])

# if __name__ == "__main__":
#     a_list = read_file('./day_07/example.txt')
#     pair = [x.split() for x in a_list]
#     print(a_list)
#     print(pair)
#     for index, item in enumerate(pair):
#         hand = item[0]
#         print(hand)
letter_map = {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}

content = read_file('./day_07/input.txt')
print(type(content))
print(content)
plays = []
for line in content:
    hand, bid = line.split()
    plays.append((hand, int(bid)))
plays.sort(key=lambda x: check_strength(x[0]))
print(plays)

total = 0

for rank, (hand, bid) in enumerate(plays, 1):
    total += rank * bid

print(total)

