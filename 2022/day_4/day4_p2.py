def get_assignments(input:str)->list:
    with open(input) as file:
        lines = file.readlines()
        assignments = [line.strip() for line in lines]
        return assignments

# for each assignment, get section 1 and section 2 as two lists.
def get_sections(assignment:str) -> tuple:
    section = assignment.split(',')
    section_1 = section[0].split('-')
    section_2 = section[1].split('-')
    return section_1,section_2

def is_in_range(set_1:set, set_2:set) -> int:
    total_num = 0
    if len(set_1.intersection(set_2))>0:
        total_num += 1
    return total_num

assignments = get_assignments('input.txt')
sum = 0
for assignment in assignments:
    sections = get_sections(assignment=assignment)
    start_1 = int(sections[0][0])
    end_1 = int(sections[0][1])
    start_2 = int(sections[1][0])
    end_2 = int(sections[1][1])
    set_1 = set(range(start_1, end_1+1))
    set_2 = set(range(start_2, end_2+1))
    total = is_in_range(set_1=set_1, set_2=set_2)
    sum += total

print(sum)