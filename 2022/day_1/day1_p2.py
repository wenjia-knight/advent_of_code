with open('input.txt') as input:
    lines = input.readlines()

for line in lines:
    calories = [line.strip() for line in lines]

total_sum = []
each_sum = 0
for calorie in calories:
    if calorie != "":
        each_sum += int(calorie)
    else:
        total_sum.append(each_sum)
        each_sum = 0
sorted_sum = sorted(total_sum, reverse = True)
print(sum(sorted_sum[0:3]))