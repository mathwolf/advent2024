import re
import numpy as np

with open('input.txt', 'r') as f:
    reports = f.read().split('\n')

total = 0
for r in reports:
    data = np.array(re.findall(r'\d+', r), dtype=int)
    df = np.diff(data)

    if np.all(df > 0) or np.all(df < 0):
        aval = np.absolute(df)
        if np.all(aval >= 1) and np.all(aval <= 3):
            total += 1
print(total)
