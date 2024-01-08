import json

with open('data.json', 'r') as file:
    data = json.load(file)

teams = list(data.keys())
matrix = []

for row in teams:
    current_row = []
    for col in teams:
        if row != col:
            current_row.append(data[row][col]['W'])
        else:
            current_row.append('-')
    matrix.append(current_row)

header = ['   '] + teams
print(' '.join(header))
for i, row in enumerate(matrix):
    print(f'{teams[i]} {"  ".join(map(str, row))}')