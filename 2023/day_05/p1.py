def read_file(file_path: str) -> list:
    with open(file_path, 'r') as input:
        content = input.read()
        return content

content = read_file('./day_05/input.txt')
splitted_content = content.split("\n\n")
seeds_list = [int(x) for x in splitted_content[0].split(': ')[1].split()]
print("seeds list", seeds_list)

seed_to_soil_numbers = splitted_content[1].split(':')[1].strip().split('\n')
soil_to_fertilizer_numbers = splitted_content[2].split(':')[1].strip().split('\n')
fertilizer_to_water_numbers = splitted_content[3].split(':')[1].strip().split('\n')
water_to_light_numbers = splitted_content[4].split(':')[1].strip().split('\n')
light_to_temp_numbers = splitted_content[5].split(':')[1].strip().split('\n')
temp_to_humi_numbers = splitted_content[6].split(':')[1].strip().split('\n')
humi_to_loc_numbers = splitted_content[7].split(':')[1].strip().split('\n')

def get_new_list(a_list: list, b_list: list)->list:
    new_value_list = []
    for x in a_list:
        for item in b_list:
            destination_num = int(item.split()[0])
            source_num = int(item.split()[1])
            length = int(item.split()[2])
            if int(x) >= source_num and int(x) <= source_num+length:
                new_value = (int(x)-source_num+destination_num)
                break
            else:
                new_value = (int(x))
        new_value_list.append(new_value)
    return new_value_list

# soil = get_new_list(a_list=seeds_list, b_list=seed_to_soil_numbers)
soil = get_new_list(a_list=seeds_list, b_list=seed_to_soil_numbers)
fertilizer = get_new_list(a_list=soil, b_list=soil_to_fertilizer_numbers)
water = get_new_list(a_list=fertilizer, b_list=fertilizer_to_water_numbers)
light = get_new_list(a_list=water, b_list=water_to_light_numbers)
temp = get_new_list(a_list=light, b_list=light_to_temp_numbers)
humi = get_new_list(a_list=temp, b_list=temp_to_humi_numbers)
loc = get_new_list(a_list=humi, b_list=humi_to_loc_numbers)

print(sorted(loc)[0])