def read_file(file_path: str) -> list:
    with open(file_path, 'r') as input:
        content = input.readlines()
        return content

content = read_file('./day_04/input.txt')
sum = 0
dictionary = {}
for i in range(len(content)):
    dictionary[i] = 1
print(dictionary)

for index, line in enumerate(content):
    nums = line.split(': ')[1]
    print("Game " + str(index))
    winning_nums = [int(x) for x in nums.split(" | ")[0].split()]
    your_nums = [int(x) for x in nums.split(" | ")[1].split()]
    matching_nums = [num for num in your_nums if num in winning_nums ]
    number_of_matching_nums = len(matching_nums)
    print("the next", number_of_matching_nums, "cards will add one copy")
    for j in range(number_of_matching_nums):
        if index+j+1 <= len(content):
            dictionary[index+j+1] = dictionary[index+j+1] + dictionary[index]
print(dictionary)

sum = 0 
for i in range(len(dictionary)):
    sum += dictionary[i]

print(sum)
