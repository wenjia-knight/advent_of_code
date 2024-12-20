with open('input.txt') as file:
    lines = file.readlines()
    rucksacks = [line.strip() for line in lines]

rucksacks_sum = 0

for rucksack in rucksacks:
    num_items = len(rucksack)//2
    rucksack_1 = set(rucksack[:num_items])
    rucksack_2 = set(rucksack[num_items:])
    i = set.intersection(rucksack_1, rucksack_2)
    i = list(i)[0]
    if i == i.lower():
        rucksacks_sum += ord(i) -96
    else:
        rucksacks_sum += ord(i) - 38

print(rucksacks_sum)