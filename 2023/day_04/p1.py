def read_file(file_path: str) -> list:
    with open(file_path, 'r') as input:
        content = input.readlines()
        return content

content = read_file('./day_04/input.txt')
print(content)
sum = 0
for index, line in enumerate(content):
    nums = line.split(': ')[1]
    print("Game " + str(index+1))
#    winning_nums = nums.split(" | ")[0].split()
    winning_nums = [int(x) for x in nums.split(" | ")[0].split()]
    print("winning numbers: " , winning_nums)
#    your_nums = nums.split(" | ")[1].split()
    your_nums = [int(x) for x in nums.split(" | ")[1].split()]
    print("your numbers: " ,your_nums)
    matching_nums = [num for num in your_nums if num in winning_nums ]
    print("matching numbers: ", matching_nums)
    if len(matching_nums) > 0:
        sum += 2**(len(matching_nums)-1)
print(sum)


# if __name__ == "__main__":
#     a_list = read_file('./day_04/example.txt')
#     print(a_list)