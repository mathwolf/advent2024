import re
import numpy as np

def test_differences(df):
    if np.all(df > 0) or np.all(df < 0):
        aval = np.absolute(df)
        if np.all(aval >= 1) and np.all(aval <= 3):
            return True
    return False


with open('input.txt', 'r') as f:
    reports = f.read().split('\n')

total = 0
for r in reports:
    data = np.array(re.findall(r'\d+', r), dtype=int)
    df = np.diff(data)

    if test_differences(df):
        total += 1
        continue

    for n in range(len(data)):
        temp_data = np.concatenate((data[:n], data[n+1:]))
        df = np.diff(temp_data)
        if test_differences(df):
            total += 1
            break

print(total)
