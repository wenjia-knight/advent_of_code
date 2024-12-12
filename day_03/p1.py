import re

filepath = './day_03/input.txt'

with open (filepath, 'r') as f:
    data = f.read()

def calculate_memory_sum(corrupted_memory):
    # Regular expression to identify valid mul(X, Y) instructions
    pattern = r"mul\((\d+),(\d+)\)"
    
    # Find all valid matches
    matches = re.findall(pattern, corrupted_memory)
    
    # Calculate the sum of all valid multiplication results
    total_sum = sum(int(x) * int(y) for x, y in matches)
    
    return total_sum

print(calculate_memory_sum(data))