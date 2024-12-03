import re

with open('input.txt', 'r') as f:
    data = f.read()

instructions = re.findall(r'mul\(\d+,\d+\)', data)

total = 0
for i in instructions:
    n1, n2 = re.findall(r'\d+', i)
    total += int(n1) * int(n2)
print(total)
