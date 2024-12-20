def read_file(file_path: str) -> list:
    with open(file_path, 'r') as input:
        content = input.read()
        return content

content = read_file('./day_05/example.txt')
splitted_content = content.split("\n\n")
print(splitted_content)

seeds, *blocks = splitted_content
seeds = [int(x) for x in seeds.split(":")[1].split()]
print(seeds)

for block in blocks:
    ranges = [] 
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    # print(ranges)
    source_num = [ranges[x][1] for x in range(len(ranges))]
    destination_num = [ranges[x][0] for x in range(len(ranges))]
    length = [ranges[x][2] for x in range(len(ranges))]
    # print(source_num)
    # print(destination_num)
    # print(length)
    new = []
    for i in range(len(seeds)):
        for j in range(len(ranges)):
            if source_num[j] <= seeds[i] <= source_num[j] + length[j]:
                new.append(seeds[i]-source_num[j]+destination_num[j])
                break
            else:
                new.append(seeds[i])
print(new)


    # for x in seeds:
    #     for a,b,c in ranges:
    #         print(a, b, c)
