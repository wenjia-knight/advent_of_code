filepath = "./2024/day_04/input.txt"

with open (filepath, 'r') as f:
    lines = f.read().strip().split('\n')

print(lines)

n = len(lines)
m = len(lines[0])

print(m, n)

dd= []
for dx in range(-1, 2):
    for dy in range(-1, 2):
        if dx != 0 or dy != 0:
            dd.append((dx, dy))

print(dd)

def has_xmas(i,j):
    if not (1<=i<n-1 and 1<=j<m-1):
        return False
    if lines[i][j] != 'A':
        return False
    
    diag_1 = f"{lines[i-1][j-1]}{lines[i+1][j+1]}"
    diag_2 = f"{lines[i-1][j+1]}{lines[i+1][j-1]}"

    if diag_1 in ['MS', 'SM'] and diag_2 in ['MS', 'SM']:
        return True
    return False

ans = 0
for i in range(n):
    for j in range(m):
            ans += has_xmas(i, j)

print(ans)