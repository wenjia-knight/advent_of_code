from puzzle_1 import read_file

D = read_file('./day_01/example.txt')
print(D)

for item in D:
    digits = [char for char in item if char.isnumeric()]
    print(digits[0])
    # first_digit = digits[0]
    # last_digit = digits[-1]
    # print(digits[0])
    # print(digits[-1])
    # for d,val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
    #     pass