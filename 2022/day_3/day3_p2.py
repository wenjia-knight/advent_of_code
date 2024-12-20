with open('input.txt') as file:
    lines = file.readlines()
    rucksacks = [line.strip() for line in lines]
print(rucksacks)

# take out three rucksacks each time, until there is no rucksack left to take
rucksacks_sum = 0
while len(rucksacks)>0:
    rucksack_1 = set((rucksacks).pop())
    rucksack_2 = set((rucksacks).pop())
    rucksack_3 = set((rucksacks).pop())
    i = set.intersection(rucksack_1, rucksack_2, rucksack_3)
    i = list(i)[0]
    if i == i.lower():
        rucksacks_sum += ord(i) -96
    else:
        rucksacks_sum += ord(i) - 38    

print(rucksacks_sum)