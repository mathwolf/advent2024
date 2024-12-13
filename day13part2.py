import re
import numpy as np

SHIFT = 10000000000000

with open('input.txt', 'r') as f:
    machines = f.read().split('\n\n')

total = 0
for m in machines:
    lines = m.split('\n')
    a = tuple(map(int, re.findall(r'\d+', lines[0])))
    b = tuple(map(int, re.findall(r'\d+', lines[1])))
    prize = tuple(map(int, re.findall(r'\d+', lines[2])))
    prize = (prize[0] + SHIFT, prize[1] + SHIFT)
    
    matrix = np.array([a, b], dtype=int).transpose()
    try:
        v = np.linalg.solve(matrix, prize)
        # to avoid errors due to round-off,
        # check if the integer version of v is a solution
        v[0] = round(v[0])
        v[1] = round(v[1])
        if not np.any(matrix@v - prize):
            total += int(3 * v[0] + v[1])
    except:
        print('Found a singular system')
        exit()
print(total)
