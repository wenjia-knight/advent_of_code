import re

def calculate_conditional_sum(corrupted_memory):
    # Regex patterns for mul, do(), and don't() instructions
    mul_pattern = r"mul\((\d+),(\d+)\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    
    # Combine all patterns into a single regex for sequential processing
    combined_pattern = f"{mul_pattern}|{do_pattern}|{dont_pattern}"
    
    # Find all instructions in the order they appear
    instructions = re.finditer(combined_pattern, corrupted_memory)
    
    # Initialise state
    mul_enabled = True
    total_sum = 0
    
    # Process each instruction in sequence
    for match in instructions:
        if match.group(1) and match.group(2):  # Matches mul(X, Y)
            if mul_enabled:
                x, y = int(match.group(1)), int(match.group(2))
                total_sum += x * y
        elif match.group(0) == "do()":  # Matches do()
            mul_enabled = True
        elif match.group(0) == "don't()":  # Matches don't()
            mul_enabled = False
    
    return total_sum

filepath = './day_03/input.txt'

with open (filepath, 'r') as f:
    data = f.read()

result = calculate_conditional_sum(data)
print(result)
