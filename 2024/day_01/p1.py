filepath = './example.txt'

with open (filepath, 'r') as f:
    data = [list(map(int, line.split())) for line in f]

list_1 = [row[0] for row in data]
list_2 = [row[-1] for row in data]
print(sorted(list_1))
print(sorted(list_2))

distances = sum(abs(b-a) for a, b in zip(sorted(list_1), sorted(list_2)))
print(distances)