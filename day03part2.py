import re

with open('input.txt', 'r') as f:
    data = f.read()

pattern = re.compile(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)')
instructions = re.findall(pattern, data)

total = 0
enable = True
for i in instructions:
    if i == 'do()':
        enable = True
    elif i == 'don\'t()':
        enable = False
    else:
        if enable:
            n1, n2 = re.findall(r'\d+', i)
            total += int(n1) * int(n2)
print(total)
