from collections import Counter
filepath = './input.txt'

with open (filepath, 'r') as f:
    data = [list(map(int, line.split())) for line in f]

list_left = [row[0] for row in data]
list_right = [row[-1] for row in data]

total = sum(each * list_right.count(each) for each in list_left)
print(total)
